from typing import TypedDict


class HelpDeskState(TypedDict):
    employeeId: str
    employeeName: str
    issue: str

    category: str
    priority: str
    resolution: list[str]
    toolsCalled: list[str]

    reviewStatus: str
    reviewReason: str
    ticketId: str | None = None
    status: str
    agentUsed: str
    finalResponse: dict
