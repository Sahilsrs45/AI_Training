from pydantic import BaseModel, Field
 
 
class RequestAIforText(BaseModel):
    requestfromAI: str
 
 
class ResponseAIforText(BaseModel):
   
    responsefromAI: str
 