from fastapi import FastAPI
from services.customer_service import  analyze_ticket
from models.customer_model import (CustomerSupportResponse,CustomerSupportRequest)

app=FastAPI(title="CUSTOMER SUPPORT TICKET TRIANGLE",
            version="1.0.1")
@app.get("/")
def home():
    return{
        "message":"Welcome to  CUSTOMER SUPPORT TICKET TRIANGLE "
    
}
    
@app.post("/api/v1/triage-ticket",response_model=CustomerSupportResponse)
def generateResponse(request:CustomerSupportRequest):
    result=analyze_ticket(request)
    return result    