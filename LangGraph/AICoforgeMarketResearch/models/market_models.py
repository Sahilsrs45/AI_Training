from pydantic import BaseModel,Field

class MarketRequest(BaseModel):
    company:str=Field(min_length=2)
    industry:str=Field(min_length=2)
    country:str=Field(min_length=2)
    year:int=Field(ge=2020,le=2100)
    question:str=Field(min_length=10)
    
    
class ResearchResult(BaseModel):
    industry_trends:list[str]
    competitors:list[str]
    opportunities:list[str]
    research_summary:str
    
class AnalysisResult(BaseModel):
    strengths:list[str]
    weakness:list[str]
    opportunities:list[str]      
    business_recommendations:list[str]
    
    
class WriterResult(BaseModel):
    report_title:str
    executive_summary:str
    detailed_report:str
    conclusion:str

class MarketResponse(BaseModel):
    status:str
    company:str
    industry:str
    country:str
    year:int
    
    
    market_research:ResearchResult
    market_analysis:AnalysisResult
    final_report:WriterResult
    
    agents_executed:list[str]
    
    
              