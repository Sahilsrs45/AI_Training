from pydantic import BaseModel, Field
 
 
class HospitalRequest(BaseModel):
 
    message: str = Field( min_length=3)
 
    user_role: str 
    