from fastapi import FastAPI
from services.llm_service import analyze_employee_feedback
from models.ai_model import (EmployeeFeedbackRequest,EmployeeFeedbackResponse)

app=FastAPI(title="Employee performance feedback",
            version="1.0.1")
@app.get("/")
def home():
    return{
        "message":"Welcome to Employee Performance feedback "
    
}
    
@app.post("/api/v1/analyze-employee",response_model=EmployeeFeedbackResponse)
def generateResponse(request:EmployeeFeedbackRequest):
    result=analyze_employee_feedback(request)
    return result    