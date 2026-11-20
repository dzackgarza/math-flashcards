use std::io::{BufRead, BufReader, Read, Write};
use std::path::PathBuf;
use std::process::{Child, ChildStdout, Command, Stdio};
use std::sync::{Arc, Mutex};
use std::time::Instant;
use tauri::{Manager, path::BaseDirectory};
use tauri_plugin_fs::FsExt;
use tokio::sync::Semaphore;

#[derive(serde::Deserialize)]
struct Scope {
    action: String,
}

#[derive(serde::Deserialize)]
struct WorkspaceScope {
    root: PathBuf,
}

#[derive(serde::Deserialize)]
struct ManifestScope {
    session: WorkspaceScope,
}

struct RequestSlots {
    foreground: Arc<Semaphore>,
    background: Arc<Semaphore>,
    diagram: Arc<Semaphore>,
}

struct StudyHost {
    child: Child,
    output: BufReader<ChildStdout>,
}

#[derive(Default)]
struct StudyProcess(Mutex<Option<StudyHost>>);

#[derive(serde::Deserialize)]
#[serde(untagged)]
enum StudyReply {
    Success { ok: bool, result: serde_json::Value },
    Failure { ok: bool, error: serde_json::Value },
}

impl StudyHost {
    fn start(app: &tauri::AppHandle) -> Result<Self, String> {
        let started = Instant::now();
        let script = app
            .path()
            .resolve("backend.py", BaseDirectory::Resource)
            .map_err(|error| error.to_string())?;
        let python = std::fs::read_to_string(script.with_file_name("runtime.txt"))
            .map_err(|error| format!("The prepared Python runtime is missing: {error}"))?;
        let mut child = Command::new(python.trim())
            .arg("-I")
            .arg(script)
            .arg("study-host")
            .arg("--release")
            .arg(app.package_info().version.to_string())
            .stdin(Stdio::piped())
            .stdout(Stdio::piped())
            .stderr(Stdio::piped())
            .spawn()
            .map_err(|error| error.to_string())?;
        let output = BufReader::new(child.stdout.take().ok_or("Study host output is missing.")?);
        log::info!(
            "event=study-host-started pid={} elapsed_ms={}",
            child.id(),
            started.elapsed().as_secs_f64() * 1000.0
        );
        Ok(Self { child, output })
    }

    fn exchange(&mut self, payload: &str) -> Result<StudyReply, String> {
        self.child
            .stdin
            .as_mut()
            .ok_or("Study host input is closed.")?
            .write_all(format!("{payload}\n").as_bytes())
            .map_err(|error| error.to_string())?;
        let mut line = String::new();
        if self
            .output
            .read_line(&mut line)
            .map_err(|error| error.to_string())?
            == 0
        {
            let status = self.child.wait().map_err(|error| error.to_string())?;
            let mut diagnostics = String::new();
            self.child
                .stderr
                .take()
                .ok_or("Study host diagnostics are missing.")?
                .read_to_string(&mut diagnostics)
                .map_err(|error| error.to_string())?;
            return Err(format!("Study host exited with {status}: {diagnostics}"));
        }
        serde_json::from_str(&line).map_err(|error| error.to_string())
    }

    fn close(&mut self) -> Result<(), String> {
        let started = Instant::now();
        self.child.stdin.take();
        let status = self.child.wait().map_err(|error| error.to_string())?;
        log::info!(
            "event=study-host-closed pid={} status={} elapsed_ms={}",
            self.child.id(),
            status,
            started.elapsed().as_secs_f64() * 1000.0
        );
        Ok(())
    }
}

// Tauri's command boundary: https://v2.tauri.app/develop/calling-rust/
#[tauri::command]
async fn request(
    app: tauri::AppHandle,
    slots: tauri::State<'_, RequestSlots>,
    payload: String,
) -> Result<String, String> {
    let started = Instant::now();
    // Tokio bounds native backend concurrency: https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html
    let scope: Scope = serde_json::from_str(&payload).map_err(|error| {
        log::error!("event=request-invalid error={error}");
        log::logger().flush();
        error.to_string()
    })?;
    let action = scope.action.clone();
    log::info!(
        "event=request-started action={} input_bytes={}",
        action,
        payload.len()
    );
    let result: Result<String, String> = async {
        if scope.action.starts_with("study-") {
            return tauri::async_runtime::spawn_blocking(move || {
                let state = app.state::<StudyProcess>();
                let mut host = state.0.lock().map_err(|error| error.to_string())?;
                if let Some(running) = host.as_mut() {
                    if running
                        .child
                        .try_wait()
                        .map_err(|error| error.to_string())?
                        .is_some()
                    {
                        log::info!("event=study-host-reaped pid={}", running.child.id());
                        *host = None;
                    }
                }
                if host.is_none() {
                    *host = Some(StudyHost::start(&app)?);
                }
                let reply = host
                    .as_mut()
                    .ok_or("Study host was not started.")?
                    .exchange(&payload)?;
                match reply {
                    StudyReply::Success { ok: true, result } => {
                        if result.get("state").and_then(serde_json::Value::as_str) == Some("Open") {
                            let media = result
                                .get("media")
                                .and_then(serde_json::Value::as_str)
                                .ok_or("The open study store has no media path.")?;
                            let store = result
                                .get("store")
                                .and_then(serde_json::Value::as_str)
                                .ok_or("The open study store has no directory.")?;
                            app.asset_protocol_scope()
                                .allow_directory(media, true)
                                .map_err(|error| error.to_string())?;
                            app.asset_protocol_scope()
                                .allow_directory(PathBuf::from(store).join("record-assets"), true)
                                .map_err(|error| error.to_string())?;
                        }
                        serde_json::to_string(&result).map_err(|error| error.to_string())
                    }
                    StudyReply::Failure { ok: false, error } => Err(error.to_string()),
                    _ => Err("Invalid response from the Study host.".into()),
                }
            })
            .await
            .map_err(|error| error.to_string())?;
        }
        let queue = match scope.action.as_str() {
            "render-diagram" => &slots.diagram,
            "assets" | "asset-version" | "sources" | "checks" | "cached-checks" | "review"
            | "generate" | "list" | "problems" | "store-problems" | "cache-manifest" | "search"
            | "store-search" => &slots.background,
            _ => &slots.foreground,
        };
        // Background batches cannot take the foreground permit.
        let permit = queue
            .clone()
            .acquire_owned()
            .await
            .map_err(|e| e.to_string())?;
        let script = app
            .path()
            .resolve("backend.py", BaseDirectory::Resource)
            .map_err(|e| e.to_string())?;
        tauri::async_runtime::spawn_blocking(move || {
            let _permit = permit;
            let scope: Scope = serde_json::from_str(&payload).map_err(|e| e.to_string())?;
            log::info!("event=backend-started action={}", scope.action);
            let python =
                std::fs::read_to_string(script.with_file_name("runtime.txt")).map_err(|e| {
                    format!(
                        "The installed Python runtime is missing. Run just desktop-install. {e}"
                    )
                })?;
            let mut child = Command::new(python.trim())
                .arg("-I")
                .arg(&script)
                .stdin(Stdio::piped())
                .stdout(Stdio::piped())
                .stderr(Stdio::piped())
                .spawn()
                .map_err(|e| format!("Could not start the backend: {e}"))?;
            child
                .stdin
                .take()
                .ok_or("The backend input pipe is missing.")?
                .write_all(format!("{payload}\n").as_bytes())
                .map_err(|e| e.to_string())?;
            let output = child.wait_with_output().map_err(|e| e.to_string())?;
            log::info!(
                "event=backend-exited action={} status={}",
                scope.action,
                output.status
            );
            let diagnostics = String::from_utf8(output.stderr).map_err(|e| e.to_string())?;
            if !output.status.success() {
                return Err(diagnostics);
            }
            if !diagnostics.is_empty() {
                log::warn!(
                    "event=backend-diagnostic action={} message={}",
                    scope.action,
                    diagnostics
                );
            }
            if scope.action == "list" {
                let root: WorkspaceScope =
                    serde_json::from_slice(&output.stdout).map_err(|e| e.to_string())?;
                app.fs_scope()
                    .allow_directory(root.root.clone(), true)
                    .map_err(|e| e.to_string())?;
                app.asset_protocol_scope()
                    .allow_directory(root.root, true)
                    .map_err(|e| e.to_string())?;
            }
            if scope.action == "manifest" || scope.action == "cached-manifest" {
                let manifest: ManifestScope =
                    serde_json::from_slice(&output.stdout).map_err(|e| e.to_string())?;
                app.fs_scope()
                    .allow_directory(manifest.session.root.clone(), true)
                    .map_err(|e| e.to_string())?;
                app.asset_protocol_scope()
                    .allow_directory(manifest.session.root, true)
                    .map_err(|e| e.to_string())?;
            }
            String::from_utf8(output.stdout).map_err(|e| e.to_string())
        })
        .await
        .map_err(|e| e.to_string())?
    }
    .await;
    let elapsed = started.elapsed().as_secs_f64() * 1000.0;
    match &result {
        Ok(_) => {
            log::info!("event=request-completed action={action} outcome=ok elapsed_ms={elapsed}")
        }
        Err(error) => log::error!(
            "event=request-completed action={action} outcome=error elapsed_ms={elapsed} error={error}"
        ),
    }
    log::logger().flush();
    result
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    // https://docs.rs/dirs/latest/dirs/fn.state_dir.html
    let diagnostics = dirs::state_dir()
        .expect("The XDG state directory is unavailable.")
        .join("math-flashcards/diagnostics/native");
    tauri::Builder::default()
        // https://v2.tauri.app/plugin/single-instance/#focusing-on-new-instance
        .plugin(tauri_plugin_single_instance::init(|app, _, _| {
            let window = app.get_webview_window("main").expect("main window missing");
            window.show().expect("could not show the main window");
            window.set_focus().expect("could not focus the main window");
        }))
        // https://v2.tauri.app/plugin/logging/#persisting-logs
        .plugin(
            tauri_plugin_log::Builder::new()
                .clear_targets()
                .target(tauri_plugin_log::Target::new(
                    tauri_plugin_log::TargetKind::Folder {
                        path: diagnostics,
                        file_name: Some("native".into()),
                    },
                ))
                .rotation_strategy(tauri_plugin_log::RotationStrategy::KeepAll)
                .level(log::LevelFilter::Info)
                .build(),
        )
        .manage(StudyProcess::default())
        .manage(RequestSlots {
            foreground: Arc::new(Semaphore::new(1)),
            background: Arc::new(Semaphore::new(1)),
            diagram: Arc::new(Semaphore::new(1)),
        })
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_store::Builder::default().build())
        .plugin(tauri_plugin_fs::init())
        .setup(|app| {
            log::info!(
                "event=app-start release={} pid={} os={} arch={}",
                app.package_info().version,
                std::process::id(),
                std::env::consts::OS,
                std::env::consts::ARCH
            );
            log::logger().flush();
            // Learning data belongs to the Python store; the webview is disposable.
            // https://docs.rs/tauri/latest/tauri/webview/struct.WebviewWindowBuilder.html#method.data_directory
            let window = app
                .config()
                .app
                .windows
                .iter()
                .find(|window| window.label == "main")
                .ok_or("The main window configuration is missing.")?;
            tauri::WebviewWindowBuilder::from_config(app, window)?
                .data_directory(app.path().app_cache_dir()?.join("webview"))
                .build()?;
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![request])
        .build(tauri::generate_context!())
        .expect("error while building tauri application")
        .run(|app, event| {
            if let tauri::RunEvent::Exit = event {
                let state = app.state::<StudyProcess>();
                if let Some(mut host) = state.0.lock().expect("study process lock failed").take() {
                    host.close().expect("could not close the study host");
                }
                log::info!("event=app-exit pid={}", std::process::id());
                log::logger().flush();
            }
        });
}
