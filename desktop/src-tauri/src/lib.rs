use std::io::Write;
use std::path::PathBuf;
use std::process::{Command, Stdio};
use std::sync::Arc;
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
}

// Tauri's command boundary: https://v2.tauri.app/develop/calling-rust/
#[tauri::command]
async fn request(
    app: tauri::AppHandle,
    slots: tauri::State<'_, RequestSlots>,
    payload: String,
) -> Result<String, String> {
    // Tokio bounds native backend concurrency: https://docs.rs/tokio/latest/tokio/sync/struct.Semaphore.html
    let scope: Scope = serde_json::from_str(&payload).map_err(|e| e.to_string())?;
    let queue = match scope.action.as_str() {
        "assets" | "sources" | "checks" | "review" | "generate" | "list" | "problems"
        | "store-problems" | "cache-manifest" | "search" | "store-search" => &slots.background,
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
        eprintln!("Backend request: {}", scope.action);
        let python =
            std::fs::read_to_string(script.with_file_name("runtime.txt")).map_err(|e| {
                format!("The installed Python runtime is missing. Run just desktop-install. {e}")
            })?;
        let mut child = Command::new(python.trim())
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
        eprintln!("Backend result: {} {}", scope.action, output.status);
        let diagnostics = String::from_utf8(output.stderr).map_err(|e| e.to_string())?;
        if !output.status.success() {
            return Err(diagnostics);
        }
        if scope.action == "list" {
            let root: WorkspaceScope =
                serde_json::from_slice(&output.stdout).map_err(|e| e.to_string())?;
            app.fs_scope()
                .allow_directory(root.root, true)
                .map_err(|e| e.to_string())?;
        }
        if scope.action == "manifest" || scope.action == "cached-manifest" {
            let manifest: ManifestScope =
                serde_json::from_slice(&output.stdout).map_err(|e| e.to_string())?;
            app.fs_scope()
                .allow_directory(manifest.session.root, true)
                .map_err(|e| e.to_string())?;
        }
        String::from_utf8(output.stdout).map_err(|e| e.to_string())
    })
    .await
    .map_err(|e| e.to_string())?
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .manage(RequestSlots {
            foreground: Arc::new(Semaphore::new(1)),
            background: Arc::new(Semaphore::new(1)),
        })
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_store::Builder::default().build())
        .plugin(tauri_plugin_fs::init())
        .invoke_handler(tauri::generate_handler![request])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
