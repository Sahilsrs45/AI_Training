
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


# Common employee fields
class EmployeeBase(BaseModel):

    employee_name: str = Field(min_length=3, max_length=100)

    department: str = Field(min_length=2, max_length=100)

    designation: str = Field(min_length=2, max_length=100)

    salary: Decimal = Field(gt=0)

    performance_rating: float = Field(ge=1, le=5)

    projects_completed: int = Field(ge=0)

    attendance_percentage: float = Field(ge=0, le=100)

    review_year: int = Field(ge=2000, le=2100)


# Create schema
class EmployeeCreate(EmployeeBase):

    pass


# Update schema
class EmployeeUpdate(BaseModel):

    pass

# Response schema
class EmployeeResponse(EmployeeBase):

    employee_id: int

    model_config = ConfigDict(from_attributes=True)


# Department average response
class DepartmentAverage(BaseModel):

    department: str

    average_rating: float


# Performance classification response
class EmployeeClassification(EmployeeResponse):

    performance_category: str
