from fastapi import FastAPI
from models.leave_model import LeaveRequest, LeaveResponse
from workflow.ai_workflow import workflow_graph

app = FastAPI(title='AI Employee Leave Request Analyzer', version='1.0')

@app.get('/')
def home():
    return {'application':'AI Employee Leave Request Analyzer','description':'Analyzes leave requests and recommends HR action'}

@app.get('/health')
def health():
    return {'status':'Running'}

@app.post('/analyze-leave', response_model=LeaveResponse)
def analyze_leave_api(data: LeaveRequest):
    result = workflow_graph.invoke({
        'employee_id': data.employee_id,
        'employee_name': data.employee_name,
        'leave_type': data.leave_type,
        'number_of_days': data.number_of_days,
        'reason': data.reason
    })
    return LeaveResponse(
        employee_id=data.employee_id,
        category=result['category'],
        summary=result['summary'],
        recommended_action=result['recommended_action'],
        status=result['status']
    )
