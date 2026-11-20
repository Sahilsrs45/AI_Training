from pydantic import BaseModel,Field
from typing import Literal

class PythonAIRequest(BaseModel):
    learner_name:str
    question:str
    experience_level:str=Literal["Fresher","Intermediate","Experienced"]


class PythonAIResponse(BaseModel):
    learner_name:str
    role:str
    answer:str    
    