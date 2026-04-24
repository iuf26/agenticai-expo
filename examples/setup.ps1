# Setup script for agenticai-expo examples (Windows PowerShell)

Write-Host "Checking Python installation..."
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is not installed. Install it from https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

Write-Host "Creating virtual environment..."
python -m venv "$PSScriptRoot\.venv"

Write-Host "Activating virtual environment..."
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"

Write-Host "Installing dependencies..."
pip install -r "$PSScriptRoot\requirements.txt"

Write-Host "Checking Node.js installation (needed for MCP Inspector)..."
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "Warning: Node.js is not installed. Install it from https://nodejs.org/ to use 'mcp dev' (MCP Inspector)." -ForegroundColor Yellow
    Write-Host "The MCP server itself (python server.py) will still work without Node.js." -ForegroundColor Yellow
} else {
    Write-Host "Node.js found: $(node --version)" -ForegroundColor Green
    Write-Host "You can test MCP servers interactively with: npx @modelcontextprotocol/inspector python server.py" -ForegroundColor Cyan
}

Write-Host "Done! Virtual environment is active and ready." -ForegroundColor Green
Write-Host "If you open a new terminal, activate it with: .\examples\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow

$currentKey = $env:OPENAI_API_KEY
if (-not $currentKey) {
    Write-Host ""
    $key = Read-Host "Enter your OpenAI API key (press Enter to skip)"
    if ($key) {
        $env:OPENAI_API_KEY = $key
        Write-Host "OPENAI_API_KEY set for this session." -ForegroundColor Green
    } else {
        Write-Host "Skipped. Set it later with: `$env:OPENAI_API_KEY = 'your-key-here'" -ForegroundColor Yellow
    }
} else {
    Write-Host "OPENAI_API_KEY is already set." -ForegroundColor Green
}
