# Day 4 — Tool Calling

Part of [ai-agents-self-learning-and-progress](../README.md).

Function calling implementation connecting LLMs to external APIs for weather and time information.

## What I Learned

- How to define tools/functions for LLMs
- Function calling workflow and tool execution
- Connecting LLMs to real-world APIs
- Multi-step tool execution in conversations

## Concepts Covered

- **Function Calling**: Defining and executing tools through LLM
- **Tool Definitions**: JSON schema for function parameters
- **API Integration**: Connecting to external services
- **Tool Loop**: Handling multiple tool calls in sequence
- **Message History**: Managing tool results in conversation

## Files and Purpose

- `ai-weather-agent.py`: Advanced weather and time agent
  - Defines real API integrations (WeatherAPI, TimeAPI)
  - Implements tool calling loop
  - Handles multiple tool execution
  - Manages conversation state with tool results

- `main.py`: Basic tool calling demonstration
  - Simple weather tool example
  - Demonstrates tool call structure
  - Shows argument extraction
  - Manual tool execution

## Key Learnings

1. **Tool Definitions**: Clear function descriptions improve LLM tool selection
2. **Parameter Schemas**: JSON schemas define required and optional parameters
3. **Tool Loop**: LLMs can chain multiple tool calls
4. **Result Handling**: Tool results must be fed back to LLM for final answer
5. **Real APIs**: Function calling enables real-world data access

## Run Instructions

### Prerequisites

- Python 3.8+
- Ollama installed and running
- Llama 3.2 model pulled: `ollama pull llama3.2`
- WeatherAPI key (for ai-weather-agent.py)

### Installation

```bash
pip install ollama requests
```

### Running the Applications

**Basic Tool Demo:**
```bash
python main.py
```

**Advanced Weather Agent:**
```bash
python ai-weather-agent.py
```

### Usage

**main.py:**
- Demonstrates basic tool calling structure
- Shows how LLM requests tool execution
- Manual tool execution demonstration

**ai-weather-agent.py:**
- Asks about weather and time in Bangalore
- Automatically executes weather and time tools
- Handles tool results and generates final answer
- Supports any city for weather queries

## Future Improvements

- Add more tools (stock prices, news, etc.)
- Implement tool error handling and retries
- Add tool permission system
- Support async tool execution
- Add tool caching for performance
- Implement tool discovery
- Add tool documentation generation
- Support streaming tool results

## Dependencies

- `ollama`: Python library for Ollama API
- `requests`: HTTP library for API calls
- `json`: Built-in Python library

## Technical Notes

### ai-weather-agent.py
- Uses WeatherAPI for historical weather data
- Uses TimeAPI for current Unix timestamp
- Implements automatic tool calling loop
- Handles multiple tool calls in single response
- Manages message history with tool results

### main.py
- Demonstrates tool call structure extraction
- Shows manual tool execution
- Educational example for understanding tool calling

### Tool Definition Structure

```json
{
  "type": "function",
  "function": {
    "name": "function_name",
    "description": "What the function does",
    "parameters": {
      "type": "object",
      "properties": {
        "param": {
          "type": "string",
          "description": "Parameter description"
        }
      },
      "required": ["param"]
    }
  }
}
```

## API Keys

The weather agent requires a WeatherAPI key. Get one free at:
https://www.weatherapi.com/

Replace the API key in `ai-weather-agent.py`:
```python
WEATHER_API_KEY = "your-api-key-here"
```
