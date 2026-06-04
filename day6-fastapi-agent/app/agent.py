from app.llm import call_llm, call_llm_with_messages


def run_agent(prompt: str) -> str:
    result = call_llm(prompt)

    return result

def run_chat(messages: list) -> str:
    result = call_llm_with_messages(messages)

    return result
