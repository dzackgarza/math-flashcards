use std::io::Write;
use std::path::PathBuf;
use std::process::{Command, Stdio};
use tauri::{Manager, path::BaseDirectory};
use tauri_plugin_fs::FsExt;

#[derive(serde::Deserialize)]
struct Scope {
    action: String,
}

#[derive(serde::Deserialize)]
struct WorkspaceScope {
    root: PathBuf,
}

// Tauri's command boundary: https://v2.tauri.app/develop/calling-rust/
#[tauri::command]
async fn request(app: tauri::AppHandle, payload: String) -> Result<String, String> {
    let script = app
        .path()
        .resolve("backend.py", BaseDirectory::Resource)
        .map_err(|e| e.to_string())?;
    tauri::async_runtime::spawn_blocking(move || {
        let scope: Scope = serde_json::from_str(&payload).map_err(|e| e.to_string())?;
        let mut child = Command::new("uv")
            .args(["run", "--locked", "--script"])
            .arg(script)
            .stdin(Stdio::piped())
            .stdout(Stdio::piped())
            .stderr(Stdio::piped())
            .spawn()
            .map_err(|e| format!("Could not start uv: {e}"))?;
        child
            .stdin
            .take()
            .ok_or("The backend input pipe is missing.")?
            .write_all(format!("{payload}\n").as_bytes())
            .map_err(|e| e.to_string())?;
        let output = child.wait_with_output().map_err(|e| e.to_string())?;
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
        String::from_utf8(output.stdout).map_err(|e| e.to_string())
    })
    .await
    .map_err(|e| e.to_string())?
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_store::Builder::default().build())
        .plugin(tauri_plugin_fs::init())
        .invoke_handler(tauri::generate_handler![request])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
