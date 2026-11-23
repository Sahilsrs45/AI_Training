from pydantic import BaseModel, Field
from typing import Literal

class LoanRequest(BaseModel):
    customer_name:str
    customer_category:Literal["Regular","Salary Account Holder","Senior Citizen","Premium","Bank Employee"]
    loan_type:str
    loan_amount:float=Field(ge=50000,le=5000000)
    annual_interest_rate:float=Field(ge=7,le=18)
    loan_tenure_years:int=Field(ge=1,le=30)
