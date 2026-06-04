# agent.py

import json
import ollama

from tools import (
    calculate_expenses,
    categorize_expenses,
    save_report
)

MAX_STEPS = 10

TOOLS = {
    "calculate_expenses": calculate_expenses,
    "categorize_expenses": categorize_expenses,
    "save_report": save_report
}

TOOLS_LIST = [

    {
        "type": "function",
        "function": {
            "name": "calculate_expenses",
            "description": """
            Calculate total expenses from structured expense data.
            The model should extract expenses from user text
            and pass them as structured JSON.
            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "expenses": {
                        "type": "object",
                        "description": """
                        Expense dictionary.

                        Example:
                        {
                            "Food": 250,
                            "Uber": 340
                        }
                        """
                    }
                },
                "required": ["expenses"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "categorize_expenses",
            "description": "Categorize expense items into categories",
            "parameters": {
                "type": "object",
                "properties": {
                    "expenses": {
                        "type": "object",
                        "description": "Expense dictionary"
                    }
                },
                "required": ["expenses"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "save_report",
            "description": "Save report into a text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "report": {
                        "type": "string",
                        "description": "Final report text"
                    }
                },
                "required": ["report"]
            }
        }
    }
]


def run_agent(user_input):

    messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]

    step = 0

    while step < MAX_STEPS:

        step += 1

        print(f"\n{'='*50}")
        print(f"STEP {step}")
        print(f"{'='*50}")

        response = ollama.chat(
            model="llama3.2",
            messages=messages,
            tools=TOOLS_LIST
        )

        message = response.message

        print("\nMODEL RESPONSE:")
        print(message)

        # =========================
        # TOOL CALLS
        # =========================

        if message.tool_calls:

            # append assistant message
            messages.append(message)

            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                print("\nTOOL CALL DETECTED")
                print("Tool:", tool_name)
                print("Arguments:", arguments)

                tool_function = TOOLS[tool_name]

                try:

                    result = tool_function(**arguments)

                    print("\nTOOL RESULT:")
                    print(result)

                    messages.append({
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": json.dumps(result)
                    })

                except Exception as e:

                    error_result = {
                        "error": str(e)
                    }

                    print("\nTOOL ERROR:")
                    print(error_result)

                    messages.append({
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": json.dumps(error_result)
                    })

        else:

            print("\nFINAL ANSWER:")
            print(message.content)

            break

    else:
        print("\nAgent exceeded max steps")