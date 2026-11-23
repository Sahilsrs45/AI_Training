from pydantic import BaseModel
from typing import List, Literal


class FoodItem(BaseModel):
    food_name: str
    quantity: int


class OrderRequest(BaseModel):
    employee_id: str
    employee_name: str
    items: List[FoodItem]


class EscalationResponse(BaseModel):

    priority: Literal["HIGH", "CRITICAL"]

    recipient: str

    escalation_message: str


class OrderResponse(BaseModel):

    order_id: str

    invoice_number: str

    employee_id: str

    employee_name: str

    subtotal: float

    gst: float

    total_amount: float

    status: str


class DelayResponse(BaseModel):

    order_id: str

    employee_id: str

    elapsed_minutes: int

    expected_minutes: int

    delay_minutes: int

    priority: str

    escalated_to: str

    message: str