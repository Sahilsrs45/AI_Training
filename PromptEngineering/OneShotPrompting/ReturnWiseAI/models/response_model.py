from pydantic import BaseModel,Field
from typing import Literal
from models.analysis_model import RetrunAnalysis
class ReturnResponse(BaseModel):
    request_id:str
    analysis:RetrunAnalysis
    recommended_next_steps:list[str]
    human_review_required:bool
    customer_message_draft:str