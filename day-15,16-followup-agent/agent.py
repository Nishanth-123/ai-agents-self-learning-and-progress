from ollama import chat


def generate_followup(email):
    thread = []

    for message in email.thread_messages:
        thread.append(
            f"""
Role: {message.role}
Sender: {message.sender}
Time: {message.sent_at}

{message.body.strip()}
"""
        )

    thread_text = "\n\n-----\n\n".join(thread)

    prompt = f"""
You are an expert professional email writer.

Your task is to draft ONE follow-up email.

## Context

Your name:
{email.your_name}

Recipient:
{email.recipient_name}

Recipient company:
{email.company_name}

Recipient email:
{email.recipient_email}

Role applied for:
{email.role_applied}

Email subject:
{email.subject}

Original sent date:
{email.sent_at}

Conversation thread:

{thread_text}

## Requirements

- Assume the recruiter has NOT replied.
- This is the first follow-up.
- Sound polite and confident.
- Express continued interest.
- Do NOT sound desperate.
- Do NOT invent facts.
- Do NOT include placeholders like [Company Name].
- Do NOT mention interviews unless already discussed.
- Keep it under 120 words.

## Output format

Return ONLY valid JSON.

{{
  "subject": "<subject>",
  "body": "<plain text email body>"
}}
"""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]
