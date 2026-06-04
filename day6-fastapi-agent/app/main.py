from fastapi import FastAPI
from app.models import AgentRequest, AgentResponse, ChatRequest
from fastapi.middleware.cors import CORSMiddleware
from app.agent import run_agent, run_chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Agent Backend Running"}


@app.post("/agent", response_model=AgentResponse)
def agent_endpoint(request: AgentRequest):
    result = run_agent(request.prompt)

    return AgentResponse(result=result)

@app.post("/summarize", response_model=AgentResponse)
def summarize_endpoint(request: AgentRequest):
    result = run_agent(f"Summarize this: {request.prompt}")

    return AgentResponse(result=result)

@app.post("/chat", response_model=AgentResponse)
def chat_endpoint(request: ChatRequest):
    result = run_chat(request.messages)

    return AgentResponse(result=result)
     