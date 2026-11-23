from fastapi import APIRouter

from models.employee_models import BatchEmployeeRequest
from services.employee_service import evaluate_employees

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


@router.post("/batch-evaluation")
def evaluate(request: BatchEmployeeRequest):
    return evaluate_employees(request.employees)