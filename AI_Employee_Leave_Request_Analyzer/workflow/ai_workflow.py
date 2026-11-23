from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from models.leave_model import LeaveRequest
from services.llm_service import analyze_leave

class LeaveState(TypedDict):
    employee_id:str
    employee_name:str
    leave_type:str
    number_of_days:int
    reason:str
    category:str
    summary:str
    recommended_action:str
    status:str

def validate_request(state: LeaveState):
    return state

def analyze_leave_node(state: LeaveState):
    request = LeaveRequest(
        employee_id=state['employee_id'],
        employee_name=state['employee_name'],
        leave_type=state['leave_type'],
        number_of_days=state['number_of_days'],
        reason=state['reason']
    )
    result = analyze_leave(request)
    return {'category': result.category, 'summary': result.summary}

def recommend_action(state: LeaveState):
    action = 'Send to HR and manager for prompt review.' if state['category']=='Urgent' else 'Forward to HR for standard review.'
    return {'recommended_action': action, 'status': 'Processed'}

workflow = StateGraph(LeaveState)
workflow.add_node('validate_request', validate_request)
workflow.add_node('analyze_leave', analyze_leave_node)
workflow.add_node('recommend_action', recommend_action)
workflow.add_edge(START, 'validate_request')
workflow.add_edge('validate_request', 'analyze_leave')
workflow.add_edge('analyze_leave', 'recommend_action')
workflow.add_edge('recommend_action', END)
workflow_graph = workflow.compile()
