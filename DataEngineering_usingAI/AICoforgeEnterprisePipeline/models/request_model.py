from pydantic import BaseModel,Field

class KnowledgeRequest(BaseModel):
    question:str =Field(
        min_length=3,
        max_length=1000
    )
    
class SearchRequest(BaseModel):
    question:str =Field(
            min_length=3,
            max_length=1000
        )
    k: int=Field(
        default=3,
        ge=1,
        le=10
    )
    