from pydantic import BaseModel,Field

class LearnerRequest(BaseModel):
    learnerName:str=Field(min_length=1)
    department:str=Field(min_length=1)
    pythonScore:int=Field(ge=0,le=100)
    sqlScore:int=Field(ge=0,le=100)
    fastApiScore:int=Field(ge=0,le=100)
    attendancePercentage:float=Field(ge=0,le=100)
    assignemtsCompleted:int=Field(gt=0)
    totalAssignemts:int=Field(gt=0)
    
    
class LearnerAnalysis(BaseModel):
    averageScore:float
    performance:str
    strongestTechnology:str
    weakestTechnology:str
    technicalAssessment:str
    recommendedLearning:list[str]
    finalRecommendation: str
    
    
class LearnerResponse(BaseModel):
    learnerName:str
    department:str
    analysis:LearnerAnalysis
    finalRecommendation:str        