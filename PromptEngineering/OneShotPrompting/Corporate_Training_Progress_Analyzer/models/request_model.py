from pydantic import BaseModel,Field

class LearnerProgressRequest(BaseModel):
    learner_id:str
    learner_name:str
    training_program:str
    topics_completed:list[str]
    assignments_assigned:int=Field(ge=0)
    assignments_completed:int=Field(ge=0)
    attendance_percentage:float=Field(ge=0 , le=100)
    coding_assesment_score:float=Field(ge=0 , le=100)
    trainer_feedback:str



