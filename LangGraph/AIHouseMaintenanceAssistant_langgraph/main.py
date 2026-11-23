from fastapi import FastAPI
from models.maintenance_model import MaintenanceRequest, MaintenanceResponse
from workflow.maintenance_workflow import workflow_graph

app = FastAPI(
    title="House Maintenance Bill Assistant"
)

@app.post("/ask-question", response_model=MaintenanceResponse)
def ask_question(request: MaintenanceRequest):

    result = workflow_graph.invoke(
        {
            "question": request.question
        }
    )

    return MaintenanceResponse(
        question = result["question"],
        answer = result["answer"]
    )


@app.get("/health")
def health():
    return {"status": "healthy"}
