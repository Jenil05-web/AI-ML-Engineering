# Activation script for the llm_env virtual environment (PowerShell)
# Place this file in the workspace root and run:
# & .\activate_llm_env.ps1

$venvActivate = Join-Path $PSScriptRoot 'llm_env\Scripts\Activate.ps1'
if (Test-Path $venvActivate) {
    Write-Host "Activating llm_env from: $venvActivate"
    & $venvActivate
} else {
    Write-Error "Activation script not found at: $venvActivate`nEnsure the virtualenv folder 'llm_env' exists in the workspace root."
}

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& "C:\Users\jenil\OneDrive\Desktop\Machine learning\activate_llm_env.ps1"