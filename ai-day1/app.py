import ollama

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

while True:
    user_input = input("You: ")

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model='llama3.2',
        messages=messages
    )

    reply = response['message']['content']

    print("AI:", reply)

    messages.append({
        "role": "assistant",
        "content": reply
    })