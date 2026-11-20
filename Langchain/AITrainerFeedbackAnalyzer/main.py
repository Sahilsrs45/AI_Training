from fastapi import FastAPI
from models.trainer_feedback_model import TrainerFeedbackResponse,TrianerFeedbackRequest
from services.llm_service import analyze_feedback

app=FastAPI(title="Trainer feedback analyzer",
            version="1.0.1")


@app.get("/")
def home():
    return{
        "message":"Welcome to feedback analyzer"
    }
    
@app.post("/api/v1/oneShot", response_model=TrainerFeedbackResponse)
def generateResponse(request: TrianerFeedbackRequest):
    result = analyze_feedback(request)
    return result        