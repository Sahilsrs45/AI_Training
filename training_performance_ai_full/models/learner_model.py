from pydantic import BaseModel, Field, model_validator

class LearnerRequest(BaseModel):
    learnerName:str
    department:str
    pythonScore:int=Field(ge=0,le=100)
    sqlScore:int=Field(ge=0,le=100)
    fastapiScore:int=Field(ge=0,le=100)
    attendancePercentage:float=Field(ge=0,le=100)
    assignmentsCompleted:int=Field(ge=0)
    totalAssignments:int=Field(ge=0)

    @model_validator(mode="after")
    def validate_assignments(self):
        if self.assignmentsCompleted>self.totalAssignments:
            raise ValueError("completed assignments cannot exceed total")
        return self

class LearnerAnalysis(BaseModel):
    averageScore:float
    performanceLevel:str
    strongestTechnology:str
    weakestTechnology:str
    technicalAssessment:str
    recommendedLearning:list[str]

class LearnerResponse(BaseModel):
    learnerName:str
    department:str
    analysis:LearnerAnalysis
    finalRecommendation:str
