from pydantic import BaseModel, Field
from typing import Literal


class HelpdeskRequest(BaseModel):
    employee_id: int = Field(gt=0)
    employee_name: str = Field(min_length=2)
    issue_type: str = Field(min_length=3)
    issue_description: str = Field(min_length=10)


class HelpdeskAnalysis(BaseModel):
    category: Literal["Password", "Network", "Software", "Other"]
    severity: Literal["Low", "Medium", "High"]
    needs_escalation: bool
    summary: str


class HelpdeskResponse(BaseModel):
    employee_id: int
    employee_name: str
    analysis: HelpdeskAnalysis
    suggested_steps: list[str]
    escalation_message: str
    status: Literal["success"]