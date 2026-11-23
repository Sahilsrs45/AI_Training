from pydantic import BaseModel, Field
from typing import List


class EmployeeRequest(BaseModel):
    employee_id: int
    employee_name: str
    department: str
    designation: str
    experience: float
    technical_skills: List[str]
    performance_rating: float = Field(ge=1, le=5)
    attendance_percentage: float = Field(ge=0, le=100)
    projects_completed: int = Field(ge=0)
    manager_feedback: str


class BatchEmployeeRequest(BaseModel):
    employees: List[EmployeeRequest]