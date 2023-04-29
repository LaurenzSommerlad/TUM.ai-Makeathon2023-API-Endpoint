from fastapi import FastAPI

app = FastAPI()

@app.post("/ask")
async def root():
    return {"message": "Hello World"}

@app.post("/report")
async def root():
    return {"message": "Hello World"}