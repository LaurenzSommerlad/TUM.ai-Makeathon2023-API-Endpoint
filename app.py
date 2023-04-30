from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Json, ValidationError
from typing import Any
from logic import build_question
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv
from static_questions import question_ctr

app = FastAPI()

class AskItem(BaseModel):
    context: Json[Any]

@app.post("/ask")
async def askEndpoint(item: AskItem):
    print(item)
    report, context, filename = build_question(item.context)
    print({"report": report, "context": context, "filename": filename})
    if report == 0:
        return {"report": report, "context": context}
    else: 
        return {"report": report, "context": context, "filename": filename}

def get_report_from_context(context):
    ans = ""
    for x in context:
        if x["id"] == question_ctr:
            ans = x["question"]
    return ans

@app.post("/chat")
async def chatEndpoint(item: AskItem):
    print(item)
    context = list(item.context)
    if(len(context) == 0):
        raise HTTPException(status_code=400, detail="endpoint /chat: empty history")
    l = len(item.context)
    new_question = ""
    new_response = ""
    for x in context:
        if x["id"] == l-1:
            prompt = x["response"]
            report = get_report_from_context(context)
            gptResponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "Act as a MCKinsey AI consultant."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": report}
                ]
            )
            for choice in gptResponse.choices:
                new_question += choice.message.content

            new_question = new_question.replace(":", ":\n")
            new_question = new_question.replace("\n\n", "\n")
            print(new_question)

            tmp = {"question": new_question
                , "response": new_response, "id": l}
            context.append(tmp)
            return {"report": 1, "context": context}
    raise HTTPException(status_code=400, detail="endpoint /chat: incomplete history")

@app.get("/pdf")
async def pdfDownload(filename: str):
    print(filename)
    path = "./pdfs/"+filename
    return FileResponse(path = path, media_type='application/pdf',filename=filename)
