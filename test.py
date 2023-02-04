from fastapi import FastAPI
import uvicorn

app=FastAPI()
@app.get("/info")
def info():
    return {"key":"HelloWorld"}
