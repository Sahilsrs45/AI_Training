from pydantic import BaseModel,Field

class SalaryRequest(BaseModel):
    employee_id:str=Field(min_length=1)
    employee_name:str=Field(min_length=1)
    question:str=Field(min_length=1)
    
    
class SalaryResponse(BaseModel):
            employee_id:str
            employee_name:str
            answer:str
            tools_used:list[str]