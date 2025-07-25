from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_message = data["message"]
    # Simulate response using Ollama (replace with actual integration)
    result = subprocess.run(["ollama", "run", "llama2"], input=user_message.encode(), capture_output=True)
    return {"response": result.stdout.decode("utf-8")}