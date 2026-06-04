import ollama
import json

def get_weather(city):
    return f"The weather in {city} is 72 degrees and sunny."

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to get the weather for",
                    },
                },
                "required": ["city"],
            },
        },
    }
]

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'What is weather in Bangalore?'
        }
    ],
    tools=tools
)

print(response)

tool_call = response['message']['tool_calls'][0]

function_name = tool_call['function']['name']

arguments = tool_call['function']['arguments']

print(f"Function name: {function_name}")
print(f"Arguments: {arguments}")

result = get_weather(arguments['city'])

print(result)
