
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from config.database import Base, engine, get_db
from config.logger import logger

from models.employeeperformance_model import Employee

from schemas.employeeperformance_schema import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
    DepartmentAverage,
    EmployeeClassification
)

from services import employeeperformance_service as service


# Create database tables
Base.metadata.create_all(bind=engine)


# FastAPI application
app = FastAPI(
    title="Employee Performance Management API",
    description="API for managing employee performance records",
    version="1.0.0"
)


# Common unexpected database error handler
def handle_database_error():
    logger.exception("Unexpected database operation failure")
    raise HTTPException(
        status_code=500,
        detail="Internal server error. Please try again later."
    )


# 1. Create employee performance record
@app.post(
    "/employees/",
    response_model=EmployeeResponse,
    status_code=201
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):

    try:
        return service.add_employee(db, data)

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Employee ID already exists"
        )

    except SQLAlchemyError:
        handle_database_error()


# 2. Get all employees with pagination
@app.get(
    "/employees/",
    response_model=list[EmployeeResponse]
)
def get_all_employees(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    try:
        return service.get_all_employees(db, skip, limit)

    except SQLAlchemyError:
        handle_database_error()


# 3. Get employee by ID
@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    try:
        employee = service.get_employee_by_id(db, employee_id)

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return employee

    except SQLAlchemyError:
        handle_database_error()


# 4. Update employee performance
@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    if not data.model_dump(exclude_unset=True):
        raise HTTPException(
            status_code=422,
            detail="Provide at least one field to update"
        )

    try:
        employee = service.update_employee(
            db,
            employee_id,
            data
        )

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return employee

    except SQLAlchemyError:
        handle_database_error()


# 5. Delete employee
@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    try:
        result = service.delete_employee(db, employee_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return {
            "message": "Employee deleted successfully",
            "employee_id": employee_id
        }

    except SQLAlchemyError:
        handle_database_error()


# 6. Filter employees by department
@app.get(
    "/employees/department/{department}",
    response_model=list[EmployeeResponse]
)
def filter_by_department(
    department: str,
    db: Session = Depends(get_db)
):

    try:
        return service.get_employees_by_department(
            db,
            department
        )

    except SQLAlchemyError:
        handle_database_error()


# 7. Employees with performance rating >= 4
@app.get(
    "/employees/high-performers",
    response_model=list[EmployeeResponse]
)
def get_high_performers(
    db: Session = Depends(get_db)
):

    try:
        return service.get_high_performers(db)

    except SQLAlchemyError:
        handle_database_error()


# 8. Average performance rating by department
@app.get(
    "/employees/department-average",
    response_model=list[DepartmentAverage]
)
def department_average(
    db: Session = Depends(get_db)
):

    try:
        return service.get_department_average(db)

    except SQLAlchemyError:
        handle_database_error()


# 9. Top five highest-rated employees
@app.get(
    "/employees/top-five",
    response_model=list[EmployeeResponse]
)
def top_five_employees(
    db: Session = Depends(get_db)
):

    try:
        return service.get_top_five_employees(db)

    except SQLAlchemyError:
        handle_database_error()


# 10. Employee performance classification
@app.get(
    "/employees/performance-classification",
    response_model=list[EmployeeClassification]
)
def performance_classification(
    db: Session = Depends(get_db)
):

    try:
        return service.classify_employee(db)

    except SQLAlchemyError:
        handle_database_error()


# Root endpoint
@app.get("/")
def home():

    return {
        "message": "Employee Performance Management API is running"
    }
