from fastapi import FastAPI
from services.LLM_service import generate_ai_response
from models.ai_model import (
    ResponseAIforText,
    RequestAIforText
)
 
app = FastAPI(
    title="OpenAI Endpoints running",
    version="1.1"
)
 
 
@app.get("/")
def home():
    return {
        "message": "AI Text Assistant is working"
    }
 
 
@app.post("/api/v1/generate", response_model=ResponseAIforText)
def generateResponse(request: RequestAIforText):
    result = generate_ai_response(request)
    return result