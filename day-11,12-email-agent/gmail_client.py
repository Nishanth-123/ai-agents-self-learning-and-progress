from agent import run_agent

def generate_email(contact):
    prompt = f"""
    You are helping me write a professional networking email, to send to a recruiter, targeting a company for a specific job.

    Recipient Name: {contact["Name"]}
    Company: {contact["Company"]}
    Role: {contact["Role"]}

    Return ONLY valid JSON with the following format:

    Do not include markdown.
    Do not include code fences. 
    Do not include explanations.

    Expected JSON format:

    {{
    "subject": "string",
    "body": "string"
    }}

    Keep it concise and professional.
    """

    return run_agent(prompt)
