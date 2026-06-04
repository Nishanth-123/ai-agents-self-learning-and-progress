from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class AgentRequest(BaseModel):
    prompt: str

class ChatRequest(BaseModel):
    messages: list[Message]

class AgentResponse(BaseModel):
    result: str