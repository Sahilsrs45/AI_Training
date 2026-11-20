from typing import TypedDict,Optional

from models.market_models import(
    ResearchResult,
    AnalysisResult,
    WriterResult
)

class MarketState(TypedDict,total=False):
        company:str
        industry:str
        country:str
        year:int
        question:str
        
        research_result:Optional[ResearchResult]
        analysis_result:Optional[AnalysisResult]
        writer_result:Optional[WriterResult]
        
        completed_agents:list[str]
        next_agent:str
        