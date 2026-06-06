import ollama
import json

def run_agent(prompt: str) -> str:
    result = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates emails on behalf of a job seeker, to send to recruiter, targeting a company for a specific job."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    message = result["message"]
    content = message["content"]

    print("RAW RESPONSE:")
    print(repr(content))

    return json.loads(content)