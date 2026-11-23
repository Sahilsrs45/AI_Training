from pydantic import BaseModel,Field
from typing import Literal
class FeedbackRequest(BaseModel):
    customer_id:str=Field(min_length=1)
    customer_name:str=Field(min_length=2)
    order_id:str=Field(min_length=1)
    rating:int=Field(ge=1,le=5)
    feedback:str=Field(min_length=10)
class FeedbackResponse(BaseModel):
    customer_id:str
    sentiment:Literal["Positive","Neutral","Negative"]
    issue_category:Literal["Delivery","Product","Service","Other"]
    priority:Literal["High","Normal"]
    reply:str
    status:str
