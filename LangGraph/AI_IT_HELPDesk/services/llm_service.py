from models.handler_model import (HelpdeskRequest)
from graphs.helpdesk_graph import workflow_graph
 
 
def analyze_agent(request: HelpdeskRequest):
    initial_state = {
        "employee_id": request.employee,
        "employeeName": request.employeeName,
        "issue": request.issue,
 
        "category": "",
        "priority": "",
 
        "resolution": [],
        "toolsCalled": [],
 
 
        "reviewStatus": "Not Reviewed",
        "reviewReason": "",
 
        "tickedId": None,
        "status": "Pending",
 
        "finalResponse": {}
    }
 
    result = workflow_graph.invoke(initial_state)
    return result["finalResponse"]