from fastapi import (
    FastAPI,
    HTTPException
)

from models.feedback_model import (
    FeedbackRequest,
    FeedbackResponse
)

from workflow.ai_workflow import (
    workflow_graph
)

app = FastAPI(

    title=
    "AI Customer Feedback Analyzer",

    version="1.0"
)


@app.get("/")
def home():

    return {

        "application":
        "AI Customer Feedback Analyzer",

        "description":
        "Analyze customer feedback using Azure OpenAI and LangGraph."
    }


@app.get("/health")
def health():

    return {
        "status": "Running"
    }


@app.post(
    "/analyze-feedback",
    response_model=FeedbackResponse
)
def analyze_feedback_api(
    data: FeedbackRequest
):

    try:

        result = workflow_graph.invoke({

            "customer_id":
            data.customer_id,

            "customer_name":
            data.customer_name,

            "order_id":
            data.order_id,

            "rating":
            data.rating,

            "feedback":
            data.feedback
        })

        return FeedbackResponse(

            customer_id=
            data.customer_id,

            sentiment=
            result["sentiment"],

            issue_category=
            result["issue_category"],

            priority=
            result["priority"],

            reply=
            result["reply"],

            status=
            result["status"]
        )

    except Exception:

        raise HTTPException(
            status_code=503,
            detail=
            "AI service temporarily unavailable."
        )