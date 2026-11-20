from pydantic import BaseModel,Field
from typing import Literal

class RetrunAnalysis(BaseModel):
    issue_category:Literal["Damaged","Wrong item","Quality","Other"]
    urgency:Literal["Low","Medium","High"]
    evidence_sufficiency:Literal["Sufficient","Insufficient","Unclear"]
    missing_information:list[str]
    reasoning_summary:str