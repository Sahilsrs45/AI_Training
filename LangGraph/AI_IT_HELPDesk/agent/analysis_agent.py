from typing import Literal
from pydantic import BaseModel, Field
from config.settings import llm


class IssueAnalysis(BaseModel):
    category: Literal[
        "Password", "Network", "Software", "Email", "Hardware", "Other"
    ]
    priority: Literal["Low", "Medium", "High", "Critical"]
    reason: str = Field(description="Short reason for the classification")


analysis_llm = llm.with_structured_output(IssueAnalysis)


def analysis_issue(state):

    prompt = f"""
    You are an IT Helpdesk Analysis Agent.

    Analyze the employee's IT issue.

    Category must be one of:
    Password, Network, Software, Email, Hardware, Other.

    Priority must be one of:
    Low, Medium, High, Critical.

    Employee Issue:
    {state["issue"]}
    """

    result = analysis_llm.invoke(prompt)

    return {
        "category": result.category,
        "priority": result.priority,
        "agentUsed": "Analysis Agent"
    }
