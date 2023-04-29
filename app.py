from fastapi import FastAPI
from pydantic import BaseModel, Json, ValidationError
from typing import Any
from logic import build_question

app = FastAPI()

class AskItem(BaseModel):
    context: Json[Any]

@app.post("/ask")
async def askEndpoint(item: AskItem):
    report, context = build_question(item.context)
    return {"report": report, "context": context}

@app.post("/chat")
async def chatEndpoint(item: AskItem):
    return {"message": "Hello World"}