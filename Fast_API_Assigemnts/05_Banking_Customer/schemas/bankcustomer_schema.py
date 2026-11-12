
from decimal import Decimal
from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict, EmailStr


class BankCustomerBase(BaseModel):

    customer_name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    account_number: str = Field(min_length=2, max_length=30)

    account_type: Literal["Savings", "Current"]

    branch_name: str = Field(min_length=2, max_length=100)

    balance: Decimal = Field(
        ge=0,
        max_digits=12,
        decimal_places=2
    )

    is_active: bool = True

    opened_on: date


class BankCustomerCreate(BankCustomerBase):
    pass


class BankCustomerUpdate(BaseModel):

    customer_name: str | None = Field(default=None, min_length=2, max_length=100)

    email: EmailStr | None = None

    branch_name: str | None = Field(default=None, min_length=2, max_length=100)


class BankCustomerResponse(BankCustomerBase):

    customer_id: int

    model_config = ConfigDict(from_attributes=True)
