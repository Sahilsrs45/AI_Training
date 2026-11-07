from decimal import Decimal
from pydantic import(
    BaseModel,Field,EmailStr,ConfigDict
)

class EmployeeBase(BaseModel):
    employee_name:str=Field(min_length=2)
    age:int=Field(ge=18,le=70)
    email:EmailStr
    department: str =Field(min_length=2)
    designation:str=Field(min_length=2)
    salary:Decimal=Field(ge=0,max_digits=12,decimal_places=2)
    city:str=Field(min_length=2)
    
class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    employee_id:int
    model_config=ConfigDict(from_attributes=True)
    
class DepartmentCount(BaseModel):
    department:str
    employee_count:int    
    