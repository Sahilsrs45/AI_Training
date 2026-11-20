from typing import TypedDict
 
from langgraph.graph import StateGraph, START, END
 
from services.llm_service import analyze_incident
 
 
# STEP 1: Define Graph State
 
class IncidentState(TypedDict):
 
    employee_id: str
    employee_name: str
    department: str
    issue: str
 
    category: str
    priority: str
    summary: str
    business_impact: str
    suggested_resolution: str
 
    escalation_required: bool
    email_sent: bool
    notification_message: str
    status: str
 
 
# STEP 2: Analyze Incident Node
 
def analyze_incident_node(state: IncidentState):
 
    result = analyze_incident(state)
 
    return {
        "category": result.category,
        "priority": result.priority,
        "summary": result.summary,
        "business_impact": result.business_impact,
        "suggested_resolution": result.suggested_resolution
    }
 
 
# STEP 3: Conditional Decision Function
 
def check_priority(state: IncidentState):
 
    if state["priority"] in ["Critical", "High"]:
        return "escalate"
 
    else:
        return "normal"
 
 
# STEP 4: Escalation Node
 
def escalate_incident_node(state: IncidentState):
 
    return {
        "escalation_required": True,
        "email_sent": True,
        "notification_message":
            "Email sent successfully to IT Support Team (simulated).",
        "status": "Escalated"
    }
 
 
# STEP 5: Normal Incident Node
 
def normal_incident_node(state: IncidentState):
 
    return {
        "escalation_required": False,
        "email_sent": False,
        "notification_message":
            "No email required. Suggested resolution provided.",
        "status": "Resolution Suggested"
    }
 
 
# STEP 6: Create State Graph
 
workflow = StateGraph(IncidentState)
 
 
# STEP 7: Add Nodes
 
workflow.add_node(
    "analyze",
    analyze_incident_node
)
 
workflow.add_node(
    "escalate",
    escalate_incident_node
)
 
workflow.add_node(
    "normal",
    normal_incident_node
)
 
 
# STEP 8: Define Starting Point
 
workflow.add_edge(
    START,
    "analyze"
)
 
 
# STEP 9: Add Conditional Edges
 
workflow.add_conditional_edges(
    "analyze",
    check_priority,
    {
        "escalate": "escalate",
        "normal": "normal"
    }
)
 
 
# STEP 10: Define End Points
 
workflow.add_edge("escalate", END)
 
workflow.add_edge("normal", END)
 
 
# STEP 11: Compile Graph
 
incident_graph = workflow.compile()