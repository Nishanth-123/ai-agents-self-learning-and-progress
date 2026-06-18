import json
import ollama

from gmail_tools import read_inbox
from tool_schema import READ_INBOX_TOOL

TOOLS = {
    "read_inbox": read_inbox,
}


def run_agent(prompt: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful email assistant. "
                "Use available tools when needed. "
                "After obtaining emails, summarize them clearly, "
                "highlight important information, and mention any action items."
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    # First LLM call
    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=[READ_INBOX_TOOL],
    )

    assistant_message = response["message"]
    print(f"Assistant message: {assistant_message}")
    messages.append(assistant_message)

    # Execute requested tools (if any)
    for tool_call in assistant_message.get("tool_calls", []):
        tool_name = tool_call["function"]["name"]
        arguments = tool_call["function"].get("arguments", {})
        print(f"Tool name: {tool_name}")
        print(f"Arguments: {arguments}")

        if tool_name not in TOOLS:
            print(f"Unknown tool: {tool_name}")
            raise ValueError(f"Unknown tool: {tool_name}")

        tool_result = TOOLS[tool_name](**arguments)

        messages.append(
            {
                "role": "tool",
                "name": tool_name,
                "content": json.dumps(tool_result),
            }
        )

    # Second LLM call to produce final answer
    final_response = ollama.chat(
        model="llama3.2",
        messages=messages,
    )

    return final_response["message"]["content"]