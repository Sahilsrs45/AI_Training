from fastapi import FastAPI
from models.trainer_model import (TrainerRequest, TrainerResponse)
from workflow.training_workflow import workflow_graph
 
app = FastAPI(
    title="AI Trainer Feedback Analyzer",
    version="1.1"
)
 
 
@app.get("/")
def home():
    return {"message": "AI Trainer Feedback Analyzer"}
 
 
@app.post("/api/v1/analyze", response_model=TrainerResponse)
def Analyzing(data: TrainerRequest):
    result = workflow_graph.invoke({
        "trainer_name": data.trainer_name,
        "learner_name": data.learner_name,
        "trainer_rating": data.trainer_rating,
        "trainer_feedback": data.trainer_feedback,
        "trainer_topic": data.trainer_topic
    })
 
    return TrainerResponse(
        trainer_name=result["trainer_name"],
        sentiments=result["sentiments"],
        performance_level=result["performance_level"],
        strengths=result["strengths"],
        imporvement_areas=result["imporvement_areas"],
        overall_summary=result["overall_summary"],
        action_taken=result["action_taken"],
        recommendation=result["recommendation"],
    )
 