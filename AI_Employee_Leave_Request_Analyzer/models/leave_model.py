from pydantic import BaseModel, Field
from typing import Literal

class LeaveRequest(BaseModel):
    employee_id:str = Field(min_length=1)
    employee_name:str = Field(min_length=2)
    leave_type: Literal["Annual","Sick","Emergency"]
    number_of_days:int = Field(ge=1, le=30)
    reason:str = Field(min_length=10)

class LeaveResponse(BaseModel):
    employee_id:str
    category: Literal["Normal","Urgent"]
    summary:str
    recommended_action:str
    status:str
