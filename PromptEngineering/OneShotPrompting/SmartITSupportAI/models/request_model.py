from pydantic import BaseModel,Field
class ITSupportRequest(BaseModel):
    ticket_id:str
    employee_id:str
    employee_name:str
    department:str
    issue_description:str
    affected_system:str
    ticket_status: str
    