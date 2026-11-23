from pydantic import BaseModel,Field



class RAGRequest(BaseModel):
    question:str
    
    
class RAGResponse(BaseModel):
    question:str
    answer:str
    sources:list[str]
        