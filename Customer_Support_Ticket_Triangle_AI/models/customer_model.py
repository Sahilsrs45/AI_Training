from pydantic import BaseModel,Field

class CustomerSupportRequest(BaseModel):
    ticket_id:str
    employee_name:str
    department:str
    issue_description:str

class CustomerSupportResponse(BaseModel):
    ticket_id: str 
    category: str 
    priority: str = Field( description="Priority must be Low, Medium, High, or Critical" )
    issue_summary: str 
    business_impact: str 
    suggested_resolution_steps: list[str] 
    recommended_team: str 
    escalation_required: bool 
    justification: str    
    