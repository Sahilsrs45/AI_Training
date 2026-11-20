from pydantic import BaseModel
class StudentRequest(BaseModel):
    student_id:int
    student_name:str
    course:str
    semester:int
    percentage:float
    primary_skill:str
    career_goal:str


class StudentAnalysis(BaseModel):
    student_name:str
    course:str
    semester:int
    percentage:float
    primary_skill:str
    career_goal:str
    academic_performance:str
    technical_assessment:str
    recommendation_learning:list[str]
    career_recommendation:list[str]    
    interview_preparation:list[str]
    
class StudentResponse(BaseModel):
    student_id:int    
    student_name:str
    prompting_technique:str="One Shot Prompting"
    ai_analysis:StudentAnalysis
    
    
    
    
    
    
    


