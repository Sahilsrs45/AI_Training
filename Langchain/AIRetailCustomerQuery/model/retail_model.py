from pydantic import BaseModel, Field
from typing import Literal


class CustomerRequest(BaseModel):

    customer_id: int = Field(..., gt=0)

    customer_name: str = Field(..., min_length=2)

    product_name: str = Field(..., min_length=1)

    query: str = Field(..., min_length=10)


class CustomerAnalysis(BaseModel):

    category: Literal[
        "Product",
        "Delivery",
        "Return",
        "Payment",
        "Other"
    ]

    sentiment: Literal[
        "Positive",
        "Neutral",
        "Negative"
    ]

    priority: Literal[
        "Low",
        "Medium",
        "High"
    ]

    summary: str


class CustomerResponse(BaseModel):

    customer_id: int

    customer_name: str

    analysis: CustomerAnalysis

    reply: str

    next_action: str

    status: str