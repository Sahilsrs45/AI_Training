from pydantic import BaseModel

class IncidentResponse(BaseModel):
    employee_id:str
    employee_name:str
    category:str
    priority:str
    summary:str
    business_impact:str
    suggested_resolution:str
    escalation_required:bool
    email_sent:bool
    notification_message:str
    status:str