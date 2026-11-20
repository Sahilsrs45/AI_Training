from typing import Literal
from pydantic import BaseModel
from config.settings import llm


class ReviewResult(BaseModel):
    status: Literal["Approved", "Rejected"]
    reason: str


review_llm = llm.with_structured_output(ReviewResult)


def review_resolution(state):

    prompt = f"""
    You are an IT HelpDesk Quality Review Agent.

    Employee Issue:
    {state["issue"]}

    Issue Category:
    {state["category"]}

    Suggested Resolution:
    {state["resolution"]}

    Tools Called:
    {state["toolsCalled"]}

    Review the suggested solution.

    Approve only if:
    - The solution is relevant
    - The instrcution are clear.
    - The solution is safe
    - It does not falsely claim the issue is fixed

    Reject if the solution is irrelevant, incomplete,
    unsafe, or requires human interventions.
    """

    result = review_llm.invoke(prompt)

    return {
        "reviewStatus": result.status,
        "reviewReason": result.reason,
        "agentUsed": "Review Agent"
    }
