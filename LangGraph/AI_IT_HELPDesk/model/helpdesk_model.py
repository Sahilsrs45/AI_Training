from pydantic import BaseModel, Field


class HelpDeskRequest(BaseModel):
    employeeId: str
    employeeName: str
    issue: str = Field(min_length=5)


class HelpDeskResponse(BaseModel):
    employeeId: str
    category: str
    priority: str
    toolsCalled: list[str]
    resolution: list[str]
    reviewStatus: str
    ticketId: str | None
    status: str
    agentUsed: str
