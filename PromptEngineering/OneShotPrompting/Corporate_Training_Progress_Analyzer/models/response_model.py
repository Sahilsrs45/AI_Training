from pydantic import BaseModel 
from models.analysis_model import LearnerProgressAnalysis
class LearnerProgressResponse(BaseModel):
    
     learner_id:str
     learner_name:str
     analysis:LearnerProgressAnalysis
     recommended_practice:list[str]
     next_learning_plan:str
     trainer_recommendation:str
     ai_summary:str