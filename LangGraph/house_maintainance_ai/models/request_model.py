from pydantic import BaseModel,Field

class MaintenanceRequest(BaseModel):
    
    question:str=Field(min_length=3)