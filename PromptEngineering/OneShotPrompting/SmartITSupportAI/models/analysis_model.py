from pydantic import BaseModel,Field
from typing import Literal,Optional
class ITSupportAnalysis(BaseModel):
    issue_category:Literal["VPN","Network","Hardware","Software","Email","Other"]
    priority_level: Literal["Low","Medium","High","Critical"]
    suspected_root_cause:str
    impact_level:Literal["Individual","Team","Oranization"]
    troubleshooting_steps:list[str]
    estimated_resolution_time:Optional[str] = None
    
    