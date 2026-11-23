from fastapi import FastAPI
from models.learner_model import LearnerRequest
from services.learner_service import analyze_learner

app=FastAPI(title="Training Performance AI")

@app.get("/")
def home():
    return {"message":"Training Performance AI Running"}

@app.post("/api/learners/analyze")
def analyze(request:LearnerRequest):
    return analyze_learner(request)
