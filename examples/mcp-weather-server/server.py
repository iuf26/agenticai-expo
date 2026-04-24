"""
MCP Weather Server
==================
A minimal Model Context Protocol server that provides weather tools.

This demonstrates the three MCP primitives:
- Tools: Functions the agent can call (get_weather, get_forecast)
- Resources: Data the agent can read (city list)
- Prompts: Pre-built templates (weather report)

Requirements: pip install mcp
"""

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP(
    name="weather-server",
    version="1.0.0",
)

# --- Simulated weather data ---
WEATHER_DATA = {
    "amsterdam": {"temp": 18, "condition": "Partly cloudy", "humidity": 72, "wind": "15 km/h NW"},
    "london": {"temp": 15, "condition": "Rainy", "humidity": 85, "wind": "20 km/h SW"},
    "new york": {"temp": 24, "condition": "Sunny", "humidity": 55, "wind": "10 km/h E"},
    "tokyo": {"temp": 22, "condition": "Clear", "humidity": 60, "wind": "8 km/h SE"},
    "sydney": {"temp": 20, "condition": "Overcast", "humidity": 68, "wind": "12 km/h N"},
}


# --- MCP Tool: get_weather ---
# Tools are functions that the AI agent can CALL to perform actions.
# The agent reads the function name, docstring, and parameter types
# to decide when and how to use it.

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The name of the city (e.g., 'Amsterdam', 'London', 'Tokyo')

    Returns:
        Current weather conditions including temperature, conditions, humidity, and wind.
    """
    city_lower = city.lower()
    if city_lower in WEATHER_DATA:
        data = WEATHER_DATA[city_lower]
        return (
            f"Weather in {city}:\n"
            f"  Temperature: {data['temp']}°C\n"
            f"  Condition: {data['condition']}\n"
            f"  Humidity: {data['humidity']}%\n"
            f"  Wind: {data['wind']}"
        )
    return f"Weather data not available for '{city}'. Available cities: {', '.join(WEATHER_DATA.keys())}"


@mcp.tool()
def compare_weather(city1: str, city2: str) -> str:
    """Compare weather between two cities.

    Args:
        city1: First city name
        city2: Second city name

    Returns:
        Side-by-side weather comparison.
    """
    w1 = WEATHER_DATA.get(city1.lower())
    w2 = WEATHER_DATA.get(city2.lower())

    if not w1:
        return f"No data for {city1}"
    if not w2:
        return f"No data for {city2}"

    diff = w1["temp"] - w2["temp"]
    warmer = city1 if diff > 0 else city2

    return (
        f"Weather Comparison:\n"
        f"\n"
        f"  {city1}: {w1['temp']}°C, {w1['condition']}\n"
        f"  {city2}: {w2['temp']}°C, {w2['condition']}\n"
        f"\n"
        f"  {warmer} is {abs(diff)}°C warmer."
    )


# --- MCP Resource: available cities ---
# Resources are READ-ONLY data that the agent can access.
# Think of them like GET endpoints — they provide context.

@mcp.resource("weather://cities")
def list_cities() -> str:
    """List all cities with available weather data."""
    return "Available cities: " + ", ".join(
        city.title() for city in WEATHER_DATA.keys()
    )


# --- MCP Prompt: weather report ---
# Prompts are pre-built templates that guide the agent's behavior.
# Think of them like stored procedures — reusable instruction sets.

@mcp.prompt()
def weather_report(city: str) -> str:
    """Generate a friendly weather report for a city."""
    return f"""Please generate a friendly, conversational weather report for {city}.
Include:
- Current conditions
- What to wear
- Activity suggestions based on the weather

Use the get_weather tool to get the actual data first."""


# --- Start the server ---
if __name__ == "__main__":
    mcp.run()
