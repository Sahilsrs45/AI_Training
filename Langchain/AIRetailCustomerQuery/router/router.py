from fastapi import APIRouter

from model.retail_model import (
    CustomerRequest,
    CustomerResponse
)

from service.retail_service import (
    customer_assistance
)

router = APIRouter(
    prefix="/customer",
    tags=["Retail Customer Query Assistant"]
)


@router.post(
    "/assist",
    response_model=CustomerResponse
)
def assist_customer(
    request: CustomerRequest
):

    return customer_assistance(request)