from fastapi import FastAPI

from model.helpdesk_model import (HelpDeskRequest, HelpDeskResponse)
from graph.helpdesk_graph import workflow_graph
from service.llm_service import analyze_agent

app = FastAPI(
    title="AI IT HELPDESK",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "Ai IT Helpdesk"
    }


@app.post("/api/v1/analyze", response_model=HelpDeskResponse)
def process_helpdesk_request(request: HelpDeskRequest):
    result = analyze_agent(request)
    return result
