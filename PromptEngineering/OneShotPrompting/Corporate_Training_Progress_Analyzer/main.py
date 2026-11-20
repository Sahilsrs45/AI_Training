from fastapi import FastAPI
from models.analysis_model import LearnerProgressAnalysis
from models.request_model import LearnerProgressRequest
from models.response_model import LearnerProgressResponse
from services.ai_services import analyze_learner_progress

app=FastAPI(title="Learner Progress Analysis one shot",version="1.0.1")

@app.get("/")
def home():return{"message" : "Welcome to Home api"}


@app.post("/api/v1/oneShot", response_model=LearnerProgressResponse)
def generateResponse(request:LearnerProgressRequest):
    result = analyze_learner_progress(request)
    return result