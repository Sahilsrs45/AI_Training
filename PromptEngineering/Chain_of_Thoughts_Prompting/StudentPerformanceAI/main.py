from fastapi import FastAPI
from models.student_model import (StudentPerformanceRequest,StudentPerformanceAnalysis,StudentPerformanceResponse)
from services.llm_service import analyse_student_performance

app=FastAPI(title="Welcome to Student Performance API",version="1.0.1")

@app.get("/")
def home():
     return {"message":"Welcome to Student  Performance API"}
   

@app.post("/api/v1/student-response", response_model=StudentPerformanceResponse)
def generateResponse(request: StudentPerformanceRequest):
    result = analyse_student_performance(request)
    return result








