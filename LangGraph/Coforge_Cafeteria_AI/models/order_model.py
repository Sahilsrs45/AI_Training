from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    food_name:str
    quantity:int


class OrderRequest(BaseModel):
    employee_id:str
    employee_name:str
    items:List[OrderItem]


class EscalationResponse(BaseModel):

    priority:str
    recipient:str
    escalation_message:str


class InvoiceResponse(BaseModel):

    order_id:str
    invoice_number:str
    employee_id:str
    employee_name:str

    subtotal:float
    gst:float
    total_amount:float

    status:str