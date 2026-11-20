from fastapi import FastAPI, HTTPException
 
from models.request_model import IncidentRequest
from models.response_model import IncidentResponse
 
from workflow.incident_workflow import incident_graph
 
 
app = FastAPI(
    title="AI-Powered IT Incident Management System",
    description="Incident analysis using LangChain and LangGraph",
    version="1.0"
)
 
 
@app.get("/")
def home():
 
    return {
        "message": "IT Incident Management API is running"
    }
 
 
@app.post(
    "/api/v1/analyze-incident",
    response_model=IncidentResponse
)
def analyze_it_incident(request: IncidentRequest):
 
    try:
 
        # Step 1: Prepare initial graph state
 
        initial_state = {
            "employee_id": request.employee_id,
            "employee_name": request.employee_name,
            "department": request.department,
            "issue": request.issue
        }
 
        # Step 2: Execute LangGraph
 
        result = incident_graph.invoke(initial_state)
 
        # Step 3: Return final response
 
        return IncidentResponse(
            employee_id=result["employee_id"],
            employee_name=result["employee_name"],
 
            category=result["category"],
            priority=result["priority"],
 
            summary=result["summary"],
            business_impact=result["business_impact"],
            suggested_resolution=result["suggested_resolution"],
 
            escalation_required=result["escalation_required"],
            email_sent=result["email_sent"],
 
            notification_message=result["notification_message"],
            status=result["status"]
        )
 
    except Exception as e:
 
        raise HTTPException(
            status_code=500,
            detail=f"Incident analysis failed: {str(e)}"
        )