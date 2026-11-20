from pydantic import BaseModel,Field
from typing import Literal


class ReturnRequest(BaseModel):
    request_id:str
    order_id:str
    product_category:str
    days_since_delivery:int=Field(ge=0)
    item_price_inr:float=Field(ge=0)
    reason:str
    evidence_provided:list[str]
    customer_description:str