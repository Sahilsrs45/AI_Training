from typing import TypedDict
 
from langgraph.graph import StateGraph, START, END
 
from service.llm_service import analyze_maintenance
 
from models.request_model import MaintenanceRequest
 
 
# Step 1: Creating the state
 
class MaintenanceState(TypedDict):
 
    question: str
 
    answer: str
 
    information_available: bool
 
 
# Step 2: Analyze maintenance question
 
def analyze_maintenance_question_node(
    state: MaintenanceState
):
 
    request = MaintenanceRequest(
        question=state["question"]
    )
 
    result = analyze_maintenance(request)
 
    fallback_message = (
        "Information is not available in the House Maintenance Policy."
    )
 
    if result.answer.strip() == fallback_message:
        information_available = False
    else:
        information_available = True
 
    return {
        "answer": result.answer,
        "information_available": information_available
    }
 
 
# Step 3: Check information availability
 
def check_information_availability(state: MaintenanceState):
 
    if state["information_available"]:
        return "information_available"
 
    return "information_not_available"
 
 
# Step 4: Create response nodes
 
def information_available_node(state: MaintenanceState):
 
    return {
        "answer": state["answer"]
    }
 
 
def information_not_available_node(state: MaintenanceState):
 
    return {
        "answer": (
            "Information is not available in the House Maintenance Policy."
        )
    }
 
 
# Step 5: Create workflow
 
workflow = StateGraph(MaintenanceState)
 
 
# Step 6: Add Nodes
 
workflow.add_node(
    "analyze_maintenance_question_node",
    analyze_maintenance_question_node
)
 
workflow.add_node(
    "information_available_node",
    information_available_node
)
 
workflow.add_node(
    "information_not_available_node",
    information_not_available_node
)
 
 
# Step 7: Starting Edge
 
workflow.add_edge(
    START,
    "analyze_maintenance_question_node"
)
 
 
# Step 8: Conditional Edges
 
workflow.add_conditional_edges(
    "analyze_maintenance_question_node",
    check_information_availability,
    {
        "information_available": "information_available_node",
        "information_not_available": "information_not_available_node"
    }
)
 
 
# Step 9: Ending Edges
 
workflow.add_edge(
    "information_available_node",
    END
)
 
workflow.add_edge(
    "information_not_available_node",
    END
)
 
 
# Step 10: Compile workflow
 
workflow_graph = workflow.compile()