"""
Simple Tool Calling Example
============================
Demonstrates the fundamental pattern of an LLM calling tools.
This is the core mechanic behind all AI agents.

Requirements: pip install openai
"""

import json
import os
from openai import OpenAI

client = OpenAI()  # Uses OPENAI_API_KEY environment variable

# --- Step 1: Define Tools ---
# Tools are described as JSON schemas. The LLM reads these descriptions
# to decide WHEN to call a tool and WHAT arguments to pass.

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city. Use this when the user asks about weather conditions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. 'Amsterdam', 'London'",
                    },
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current time in a given timezone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "IANA timezone, e.g. 'Europe/Amsterdam'",
                    },
                },
                "required": ["timezone"],
            },
        },
    },
]


# --- Step 2: Implement the actual tool functions ---
# These are regular Python functions. The LLM never runs these directly —
# YOUR code executes them based on what the LLM asks for.

def get_weather(city: str) -> dict:
    """Simulate a weather API call."""
    # In production, this would call a real weather API like OpenWeatherMap
    fake_weather = {
        "Amsterdam": {"temp": 18, "condition": "Partly cloudy", "humidity": 72},
        "London": {"temp": 15, "condition": "Rainy", "humidity": 85},
        "New York": {"temp": 24, "condition": "Sunny", "humidity": 55},
    }
    weather = fake_weather.get(city, {"temp": 20, "condition": "Unknown", "humidity": 50})
    return {"city": city, **weather}


def get_time(timezone: str) -> dict:
    """Simulate a timezone API call."""
    from datetime import datetime

    return {"timezone": timezone, "current_time": datetime.now().isoformat()}


# Map tool names to functions
tool_functions = {
    "get_weather": get_weather,
    "get_time": get_time,
}


# --- Step 3: The Agent Loop ---
def run_agent(user_message: str):
    print(f"\nUser: {user_message}")
    print("Agent is thinking...\n")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Use the available tools when needed to answer questions accurately.",
        },
        {"role": "user", "content": user_message},
    ]

    # First call: LLM decides whether to use tools
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
    )

    assistant_message = response.choices[0].message

    # Check if the LLM wants to call any tools
    if assistant_message.tool_calls:
        # Add the assistant's response (with tool calls) to the conversation
        messages.append(assistant_message)

        # Execute each tool call
        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"Agent wants to call: {function_name}({arguments})")

            # Execute the tool
            if function_name in tool_functions:
                result = tool_functions[function_name](**arguments)
            else:
                result = {"error": f"Unknown tool: {function_name}"}

            print(f"Tool result: {result}\n")

            # Add tool result to conversation
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )

        # Second call: LLM generates final response using tool results
        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
        )
        print(f"Agent: {final_response.choices[0].message.content}")
    else:
        # No tools needed — direct response
        print(f"Agent: {assistant_message.content}")


# --- Run Examples ---
if __name__ == "__main__":
    # Example 1: This should trigger the weather tool
    run_agent("What's the weather like in Amsterdam?")

    print("\n" + "=" * 60 + "\n")

    # Example 2: This should trigger the time tool
    run_agent("What time is it in Europe/Amsterdam?")

    print("\n" + "=" * 60 + "\n")

    # Example 3: This should NOT trigger any tools
    run_agent("What is the capital of France?")
