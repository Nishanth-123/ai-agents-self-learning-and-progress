from ollama import chat


MODEL_NAME = "llama3.2"


def call_llm(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

def call_llm_with_messages(messages: list) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            *messages
        ]
    )

    return response["message"]["content"]
