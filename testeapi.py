from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import agent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Query(BaseModel):
    prompt: str

@app.post("/api/ask")
async def ask_agent(query: Query):
    response = agent.run(query.prompt)
    return {"resposta": response.content}

@app.get("/api/ping")
async def ping():
    return {"status": "ok"}

