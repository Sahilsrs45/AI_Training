from fastapi import FastAPI
from services.llm_service import analyze_python_role_based
from models.model_role_based import (PythonAIResponse,PythonAIRequest)

app=FastAPI(title="Role Based Prompting API",
            version="1.0.1")

@app.get("/")
def home():
    return{
        "message":"Welcome to  Role based Prompting "
    
}
    
@app.post("/api/v1/analyze-data",response_model=PythonAIResponse)
def generateResponse(request:PythonAIRequest):
    result=analyze_python_role_based(request)
    return result    