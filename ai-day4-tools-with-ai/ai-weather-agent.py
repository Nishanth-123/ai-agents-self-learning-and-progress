import ollama
import json
import requests

WEATHER_API_KEY = "340893c867d64f4fa1a13105261905"
WEATHER_BASE_URL = "https://api.weatherapi.com/v1/history.json"
TIME_BASE_URL = "https://timeapi.io/api/v1/time/current/unix"

def get_weather(city):
    url = f"{WEATHER_BASE_URL}?key={WEATHER_API_KEY}&q={city}&dt=2026-05-19"
    response = requests.get(url)
    data = response.json()
    city = data["location"]["name"]
    temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
    result = f"{city}: {temp}°C, {condition}"
    return result

def get_current_time():
    url = f"{TIME_BASE_URL}"
    response = requests.get(url)
    data = response.json()
    result = data["unix_timestamp"]
    return result

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather of a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Get current time",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}]

messages = [{"role": "user", "content": "What's weather and time in Bangalore?"}]
ollamaResponse = ollama.chat(model="llama3.2", messages=messages, tools=tools)
while ollamaResponse["message"].get("tool_calls"):
    message = ollamaResponse["message"]
    tool_calls = message["tool_calls"]
    for tool_call in tool_calls:
       if tool_call["function"]["name"] == "get_weather":
           arguments = tool_call["function"]["arguments"]
           result = get_weather(arguments["city"])
           messages.append({
               "role": "tool",
               "name": "get_weather",
               "content": result
           })
           print(f"Weather result: {result}")
           ollamaResponse = ollama.chat(model="llama3.2", messages=messages, tools=tools)
       elif tool_call["function"]["name"] == "get_current_time":
           result = get_current_time()
           messages.append({
               "role": "tool",
               "name": "get_current_time",
               "content": f"Current time in seconds is: {result}"
           })
           print(f"Time result: {result}")
           ollamaResponse = ollama.chat(model="llama3.2", messages=messages, tools=tools) 

print(ollamaResponse["message"]["content"])


