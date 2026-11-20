from pydantic import BaseModel,Field
from typing import Literal

class IncidentAnalysis(BaseModel):
    category:str
    priority:Literal["Critical","High","Medium","Low"]
    summary:str
    business_impact:str
    suggested_resolution:str
    
    