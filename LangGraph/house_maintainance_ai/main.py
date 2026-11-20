from fastapi import FastAPI
 
from models.request_model import MaintenanceRequest
from models.response_model import MaintenanceResponse
 
from agents.maintenance_agent import workflow_graph
 
 
# Creating FastAPI application
 
app = FastAPI(
    title="AI House Maintenance Bill Assistant",
    version="1.0"
)
 
 
# Home API
 
@app.get("/")
def home():
 
    return {
        "message": "AI House Maintenance Bill Assistant"
    }
 
 
# Maintenance Question API
 
@app.post("/api/v1/maintenance",response_model=MaintenanceResponse)
def analyzing(data: MaintenanceRequest):
 
    result = workflow_graph.invoke({
 
        "question": data.question,
 
        "answer": "",
 
        "information_available": False
 
    })
 
    return MaintenanceResponse(
 
        question=data.question,
 
        answer=result["answer"]
 
    )