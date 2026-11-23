from pydantic import BaseModel, Field
from typing import Literal


class ProductItem(BaseModel):
    product_id: str
    name: str

    category: Literal[
        "Grocery",
        "Household",
        "Personal Care"
    ]

    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    gst_rate: Literal[
        0,
        5,
        12,
        18
    ]


class BillingRequest(BaseModel):

    customer_name: str

    membership_tier: Literal[
        "Regular",
        "Silver",
        "Gold",
        "Platinum"
    ]

    coupon_code: str | None = None

    loyalty_points_available: int = Field(ge=0)

    loyalty_points_to_redeem: int = Field(ge=0)

    items: list[ProductItem]