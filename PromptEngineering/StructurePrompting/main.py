from fastapi import FastAPI
from services.llm_service import analyzer
from models.structure_model import LearnerResponse,LearnerRequest

app=FastAPI(title="Structured Prompting",
            version="1.0.1")

@app.get("/")
def home():
    return{
        "message":"Welcome to  Structured based Prompting "
    
}
    
@app.post("/api/v1/analyze-data",response_model=LearnerResponse)
def generateResponse(request:LearnerRequest):
    result=analyzer(request)
    return result    