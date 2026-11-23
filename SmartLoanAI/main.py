from fastapi import FastAPI
from models.loan_request import LoanRequest
from services.loan_calculator import calculate_loan

app=FastAPI(title="SmartLoan AI")

@app.get("/api/loan/health")
def health():
    return {"status":"healthy"}

@app.get("/api/loan/discounts")
def discounts():
    return {"Regular":0,"Salary Account Holder":10,"Senior Citizen":20,"Premium":30,"Bank Employee":50}

@app.post("/api/loan/calculate")
def calculate(request:LoanRequest):
    return calculate_loan(request)

@app.post("/api/loan/analyze")
def analyze(request:LoanRequest):
    return calculate_loan(request)

@app.post("/api/loan/compare")
def compare(request:LoanRequest):
    reg=request.model_copy()
    reg.customer_category='Regular'
    prem=request.model_copy()
    prem.customer_category='Premium'
    return {"regular":calculate_loan(reg),"premium":calculate_loan(prem)}
