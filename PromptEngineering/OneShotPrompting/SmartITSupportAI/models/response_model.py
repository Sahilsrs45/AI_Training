from pydantic import BaseModel,Field
from models.analysis_model import ITSupportAnalysis
class ITSupportResponse(BaseModel):
    ticket_id:str
    ticket_status:str
    analysis:ITSupportAnalysis
    recommended_actions:list[str]
    escalated_required:bool
    ai_summary:str