from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from services.llm_service import answer_question
from models.maintenance_model import (
    MaintenanceRequest,
    MaintenanceAnswer
)

# creating the state

class MaintenanceState(TypedDict):
    question: str

    answer: str


# Node : LangChain call (AI answer from the policy)
def answer_question_node(
        state: MaintenanceState
):

    request = MaintenanceRequest(
        question=state["question"]
    )

    result = answer_question(request)

    return {
        "answer": result.answer
    }


# Create Workflow

workflow = StateGraph(
    MaintenanceState
)


# Add Nodes

workflow.add_node(
    "answer_question_node",
    answer_question_node)


# Edges : START -> node -> END

workflow.add_edge(START, "answer_question_node")

workflow.add_edge("answer_question_node", END)


workflow_graph = workflow.compile()
