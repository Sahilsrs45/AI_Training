from pydantic import BaseModel,Field

class IncidentRequest(BaseModel):
    employee_id:str
    employee_name:str
    department:str
    issue:str
    
    
    