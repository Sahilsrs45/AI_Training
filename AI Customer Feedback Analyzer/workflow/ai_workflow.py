from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from models.feedback_model import (
    FeedbackRequest
)

from services.llm_service import (
    analyze_feedback
)


class FeedbackState(TypedDict):

    customer_id: str
    customer_name: str
    order_id: str
    rating: int
    feedback: str

    sentiment: str
    issue_category: str
    priority: str
    reply: str
    status: str


# Node 1
def validate_feedback(
    state: FeedbackState
):

    return state


# Node 2
def classify_feedback(
    state: FeedbackState
):

    request = FeedbackRequest(

        customer_id=state["customer_id"],

        customer_name=state["customer_name"],

        order_id=state["order_id"],

        rating=state["rating"],

        feedback=state["feedback"]
    )

    result = analyze_feedback(
        request
    )

    priority = (
        "High"
        if result.sentiment == "Negative"
        else "Normal"
    )

    return {

        "sentiment":
        result.sentiment,

        "issue_category":
        result.issue_category,

        "priority":
        priority,

        "reply":
        result.reply
    }


# Node 3
def generate_reply(
    state: FeedbackState
):

    return {
        "status": "Processed"
    }


workflow = StateGraph(
    FeedbackState
)

workflow.add_node(
    "validate_feedback",
    validate_feedback
)

workflow.add_node(
    "classify_feedback",
    classify_feedback
)

workflow.add_node(
    "generate_reply",
    generate_reply
)

workflow.add_edge(
    START,
    "validate_feedback"
)

workflow.add_edge(
    "validate_feedback",
    "classify_feedback"
)

workflow.add_edge(
    "classify_feedback",
    "generate_reply"
)

workflow.add_edge(
    "generate_reply",
    END
)

workflow_graph = workflow.compile()