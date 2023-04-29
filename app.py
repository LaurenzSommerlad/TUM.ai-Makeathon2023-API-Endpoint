from fastapi import FastAPI
from pydantic import BaseModel, Json, ValidationError
from typing import Any, Optional, List
from logic import build_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskItem(BaseModel):
    context: Any


@app.post("/ask")
async def askEndpoint(item: AskItem):
    print(item)
    report, context = build_question(item.context)
    print({"report": report, "context": context})
    return {"report": report, "context": context}


@app.post("/chat")
async def chatEndpoint(item: AskItem):
    return {"message": "Hello World"}
