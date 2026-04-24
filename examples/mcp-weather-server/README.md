# MCP Weather Server Example

A minimal Model Context Protocol (MCP) server that provides weather data. 
Connect it to VS Code (GitHub Copilot) or Claude Desktop.

## What This Demonstrates

1. Creating an MCP server with FastMCP
2. Defining tools (callable functions)
3. Defining resources (readable data)
4. Connecting to an MCP client (VS Code, Claude Desktop)

## Setup

From the repo root, run the setup script for your OS:

**Windows (PowerShell):**
```powershell
.\examples\setup.ps1
```

**macOS / Linux (Shell):**
```bash
bash examples/setup.sh
```

The setup script activates the virtual environment automatically. If you open a new terminal, activate it first:

**Windows (PowerShell):**
```powershell
.\examples\.venv\Scripts\Activate.ps1
```

**macOS / Linux (Shell):**
```bash
source examples/.venv/bin/activate
```

## Run Standalone

```bash
python server.py
```

## Connect to VS Code

Add to your VS Code `settings.json` (User or Workspace):

```json
{
  "mcp": {
    "servers": {
      "weather": {
        "command": "python",
        "args": ["<absolute-path-to>/examples/mcp-weather-server/server.py"]
      }
    }
  }
}
```

Then in GitHub Copilot Chat (Agent mode), ask: **"What's the weather in Amsterdam?"**

Copilot will discover and use your MCP server's tools automatically.
