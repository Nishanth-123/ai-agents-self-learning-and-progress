import ollama

prompt = """
You are a person applying for a frontend engineer role at high end MAANg company.

Write a recruiter outreach email,

Constraints:
- professional tone
- under 120 words
- include CTA
- mention React and TypeScript

Return:
Subject:
Body:
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])