from fastapi import FastAPI
from models.ai_model import SalaryResponse,SalaryRequest

from services.llm_service import calculate_employee_salary


app=FastAPI(title="AI Employee Salary",
            version="1.0.1")


@app.get("/")
def home():
    return{
        "message":"Welcome to AI Salary Agent"
    }

@app.post("/api/v1/agent",response_model=SalaryResponse)
def analyze_salary(request:SalaryRequest):
    result=calculate_employee_salary(request)
    
    return result
