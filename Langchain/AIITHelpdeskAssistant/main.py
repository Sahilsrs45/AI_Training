from fastapi import FastAPI

from models.helpdesk_model import (
    HelpdeskRequest,
    HelpdeskResponse
)

from service.helpdesk_service import helpdesk_analysis


app = FastAPI(
    title="AI Helpdesk Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Home Endpoint"
    }


@app.post(
    "/api/v1/helpdesk",
    response_model=HelpdeskResponse
)
def analyze_helpdesk(request: HelpdeskRequest):

    response = helpdesk_analysis(request)

    return response