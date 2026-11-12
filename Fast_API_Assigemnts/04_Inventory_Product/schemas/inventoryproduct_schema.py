
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):

    product_name: str = Field(min_length=2, max_length=100)

    category: str = Field(min_length=2, max_length=100)

    supplier_name: str = Field(min_length=2, max_length=100)

    unit_price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)

    quantity_in_stock: int = Field(ge=0)

    reorder_level: int = Field(ge=0)

    warehouse_location: str = Field(min_length=2, max_length=100)

    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):

    pass


class ProductResponse(ProductBase):

    product_id: int

    model_config = ConfigDict(from_attributes=True)
