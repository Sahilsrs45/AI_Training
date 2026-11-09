
from unicodedata import numeric

from pydantic import (BaseModel,Field,EmailStr,ConfigDict)

class EmployeeBase(BaseModel):
    EmployeeName:str=Field(min_length=3)
    Department:str=Field(min_lenght=3)
    Designation:str=Field(min_length=4)
    Salary:numeric=Field(gt=0)
    PerformanceRating:float=Field(ge=0,le=5)
    ProjectsCompleted:int=Field(ge=0 ,le=100)
    AttendancePercentage:float=Field(ge=0,le=100)
    ReviewYear:int=Field(ge=2000,le=2026)    
    
class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EMployeeResponse(EmployeeBase):
    EmployeeId:int
    model_config=ConfigDict(from_attributes=True)
    