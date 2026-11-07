from pydantic import(BaseModel,Field,EmailStr,ConfigDict)
 
class CustomerBase(BaseModel):
    CustomerName: str = Field(min_length=2)
    CustomerEmail: EmailStr
    CustomerAge: int = Field(ge=18, le=70)
    CustomerGender: str = Field(min_length=2)
 
class CustomerCreate(CustomerBase):
    pass
 
class CustomerUpdate(CustomerBase):
    pass
 
class CustomerResponse(CustomerBase):
    CustomerId: int
    model_config=ConfigDict(from_attributes=True)
 
 