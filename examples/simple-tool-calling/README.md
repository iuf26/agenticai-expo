# Simple Tool Calling Example

A minimal example showing how an LLM calls tools (functions) during a conversation.

## What This Demonstrates

1. Defining tools with JSON schema
2. Sending a user message with available tools
3. The LLM deciding to call a tool
4. Executing the tool and returning results
5. The LLM generating a final response using tool output

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

The setup script will also ask for your OpenAI API key. If you skip it, set it later:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your-key-here"
```

**macOS / Linux (Shell):**
```bash
export OPENAI_API_KEY="your-key-here"
```

## Run

```bash
python agent.py
```

## Expected Output

```
Agent is thinking...
Agent wants to call: get_weather(city='Amsterdam')
Tool result: {'city': 'Amsterdam', 'temp': 18, 'condition': 'Partly cloudy', 'humidity': 72}
Agent response: The weather in Amsterdam is currently 18°C with partly cloudy skies and 72% humidity.
```
