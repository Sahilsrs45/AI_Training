from pydantic import BaseModel, Field
from typing import Literal
 
 
class TrainerRequest(BaseModel):
    trainer_name: str
    learner_name: str
    trainer_rating: int = Field(ge=1, le=5)
    trainer_feedback: str
    trainer_topic: str
 
 
class TrainerResponse(BaseModel):
    trainer_name: str
    sentiments: Literal["Positive", "Neutral", "Negative"]
    performance_level: Literal["Excellent","Very Good", "Average", "Need Improvements"]
    strengths: str
    imporvement_areas: list[str]
    overall_summary: list[str]
    action_taken: str
    recommendation: str