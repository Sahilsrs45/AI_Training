from pydantic import BaseModel,Field

class EmployeeFeedbackRequest(BaseModel):
    employee_name:str
    reviewer_name:str
    project_name:str
    performance_rating:int=Field(ge=1,le=5)
    feedback:str
    
class EmployeeFeedbackResponse(BaseModel):
    employee_name:str
    sentiment:str
    performance_level:str
    strengths:list[str]
    improvement_areas:list[str]
    development_recommendations:list[str]
    overall_summary:str
    suggested_action:str    