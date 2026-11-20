from fastapi import FastAPI
 
from models.request_model import HospitalRequest
from models.response_model import HospitalResponse
 
from services.llm_service import manage_hospital_request
 
 
# STEP 1: CREATE FASTAPI APPLICATION
 
app = FastAPI(
    title="AI Hospital Management System",
    description="Hospital Management Assistant using LangChain Agent",
    version="1.0.0"
)
 
 
# STEP 2: HEALTH CHECK API
 
@app.get("/health")
def health_check():
 
    return {
        "status": "success",
        "message": "Hospital Management API is running"
    }
 
 
# STEP 3: HOSPITAL MANAGEMENT API
 
@app.post(
    "/hospital/ask",
    response_model=HospitalResponse
)
def hospital_assistant(request: HospitalRequest):
 
    response = manage_hospital_request(request)
 
    return response