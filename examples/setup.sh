#!/bin/bash
# Setup script for agenticai-expo examples (macOS / Linux)

# Make this script executable for future runs
chmod +x "$0"

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Install it from https://www.python.org/downloads/"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Creating virtual environment..."
python3 -m venv "$SCRIPT_DIR/.venv"

echo "Activating virtual environment..."
source "$SCRIPT_DIR/.venv/bin/activate"

echo "Installing dependencies..."
pip install -r "$SCRIPT_DIR/requirements.txt"

echo "Checking Node.js installation (needed for MCP Inspector)..."
if ! command -v node &> /dev/null; then
    echo "Warning: Node.js is not installed. Install it from https://nodejs.org/ to use 'mcp dev' (MCP Inspector)."
    echo "The MCP server itself (python server.py) will still work without Node.js."
else
    echo "Node.js found: $(node --version)"
    echo "You can test MCP servers interactively with: npx @modelcontextprotocol/inspector python server.py"
fi

echo "Done! Virtual environment is active and ready."
echo "If you open a new terminal, activate it with: source examples/.venv/bin/activate"

if [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    read -p "Enter your OpenAI API key (press Enter to skip): " key
    if [ -n "$key" ]; then
        export OPENAI_API_KEY="$key"
        echo "OPENAI_API_KEY set for this session."
    else
        echo "Skipped. Set it later with: export OPENAI_API_KEY='your-key-here'"
    fi
else
    echo "OPENAI_API_KEY is already set."
fi
