from pydantic import BaseModel,Field

class MaintenanceResponse(BaseModel):
    question:str
    answer:str