from pydantic import BaseModel,Field
from typing import Literal
class AstronautRequest(BaseModel):
    astronaut_id:str
    astronaut_name:str
    age:int=Field(ge=18, le=65)
    training_hours:int=Field(ge=0)
    medical_clearance:bool
    previous_missions:int=Field(ge=0)
    mission_type:Literal["Reasearch","Maintenance","Exploration"]
    
class AstronautAnalysis(BaseModel):
    age_eligible:bool
    training_eligible:bool
    medical_eligible:bool
    experience_eligible:bool2
    failed_checks:list[str]
    risk_level:str
         

class AstronautResponse(BaseModel):
    astronaut_id:str
    astronaut_name:str
    mission_type:str
    readiness_status:str
    risk_level:str
    reason:str
    recommendation:str    
    