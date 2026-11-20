from fastapi import FastAPI
from services.llm_service import analyze_student_profile
from models.ai_model import ( StudentRequest,StudentResponse,StudentAnalysis)

app=FastAPI(title="College Management one shot",version="1.0.1")

@app.get("/")
def home():return{"message" : "Welcome to Home api"}


@app.post("/api/v1/oneShot", response_model=StudentResponse)
def generateResponse(request: StudentRequest):
    result = analyze_student_profile(request)
    return result