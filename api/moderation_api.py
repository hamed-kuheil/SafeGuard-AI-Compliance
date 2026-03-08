
from fastapi import FastAPI

app = FastAPI()

@app.post("/moderate")
def moderate(data: dict):
    text = data["text"]
    return {"message":"Pipeline not wired in this minimal demo","input":text}
