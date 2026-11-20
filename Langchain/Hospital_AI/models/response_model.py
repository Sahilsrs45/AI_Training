from pydantic import BaseModel
from typing import Any, List
 
 
class HospitalResponse(BaseModel):
 
    status: str
 
    response: str
 
    tools_used: List[str] = []
 
    data: Any = None