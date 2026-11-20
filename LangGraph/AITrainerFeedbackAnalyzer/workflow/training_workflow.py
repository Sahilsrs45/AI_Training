from typing import TypedDict
 
from langgraph.graph import StateGraph, START, END
 
from services.trainer_service import analyze_trainer
from models.trainer_model import (
    TrainerRequest,
    TrainerResponse
)
# creating the state
 
 
class TrainingFeedbackState(TypedDict):
    trainer_name: str
    learner_name: str
    trainer_rating: int
    trainer_feedback: str
    trainer_topic: str
 
    sentiments: str
    performance_level: str
    strengths: str
    imporvement_areas: list[str]
    overall_summary: list[str]
    recommendation: str
    action_taken: str
 
 
def analyze_training_feedback_node(state: TrainingFeedbackState):
 
    request = TrainerRequest(
        trainer_name=state["trainer_name"],
        learner_name=state["learner_name"],
        trainer_rating=state["trainer_rating"],
        trainer_feedback=state["trainer_feedback"],
        trainer_topic=state["trainer_topic"]
    )
 
    result = analyze_trainer(request)
 
    return {
        "sentiments": result.sentiments,
        "performance_level": result.performance_level,
        "strengths": result.strengths,
        "imporvement_areas": result.imporvement_areas,
        "overall_summary": result.overall_summary,
        "recommendation": result.recommendation
    }
 
 
def check_trainer_performance_level(state: TrainingFeedbackState):
    if state["performance_level"] == "Needs Improvement":
        return "Change Trainer"
    return "Continue Trainer"
 
 
def change_trainer_node(state: TrainingFeedbackState):
    return {
        "action_taken": "Change Trainer"
    }
 
 
def Continue_trianer_node(state: TrainingFeedbackState):
    return {
        "action_taken": "Continue Trainer"
    }
 
 
# Step 6 Create Workflow
workflow = StateGraph(TrainingFeedbackState)
 
 
# Add Nodes
workflow.add_node(
    "analyze_training_feedback_node",
    analyze_training_feedback_node)
workflow.add_node("change_trainer_node", change_trainer_node)
workflow.add_node("Continue_trianer_node", Continue_trianer_node)
 
 
# Step 8 Starting Edge
 
workflow.add_edge(START, "analyze_training_feedback_node")
 
workflow.add_conditional_edges(
    "analyze_training_feedback_node",
    check_trainer_performance_level,
    {
        "Change Trainer": "change_trainer_node",
        "Continue Trainer": "Continue_trianer_node"
    }
)
workflow.add_edge("change_trainer_node", END)
workflow.add_edge("Continue_trianer_node", END)
workflow_graph = workflow.compile()
 