
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models.employeeperformance_model import Employee
from config.logger import logger


# 1. Create employee performance record
def add_employee(db: Session, data):

    try:
        employee = Employee(**data.model_dump())

        db.add(employee)
        db.commit()
        db.refresh(employee)

        logger.info(
            "Employee record created. Employee ID: %s",
            employee.employee_id
        )

        return employee

    except IntegrityError:
        db.rollback()

        logger.warning(
            "Duplicate employee ID: %s",
            data.employee_id
        )

        raise

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while creating employee")
        raise


# 2. Get all employees with pagination
def get_all_employees(db: Session, skip: int, limit: int):

    query = (
        select(Employee)
        .order_by(Employee.employee_id)
        .offset(skip) 
        .limit(limit)
    )

    return db.scalars(query).all()


# 3. Get employee by ID
def get_employee_by_id(db: Session, employee_id: int):

    employee = db.get(Employee, employee_id)

    if employee is None:
        logger.warning(
            "Employee not found. ID: %s",
            employee_id
        )

    return employee


# 4. Update employee performance
def update_employee(db: Session, employee_id: int, data):

    employee = db.get(Employee, employee_id)

    if employee is None:
        logger.warning(
            "Update failed. Employee not found: %s",
            employee_id
        )
        return None

    update_data = data.model_dump(exclude_unset=True)

    if not update_data:
        logger.warning("Update requested without any fields")
        return None

    try:

        for key, value in update_data.items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        logger.info(
            "Employee updated successfully. ID: %s",
            employee_id
        )

        return employee

    except IntegrityError:
        db.rollback()
        logger.exception("Integrity error while updating employee")
        raise

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while updating employee")
        raise


# 5. Delete employee
def delete_employee(db: Session, employee_id: int):

    employee = db.get(Employee, employee_id)

    if employee is None:
        logger.warning(
            "Delete failed. Employee not found: %s",
            employee_id
        )
        return False

    try:

        db.delete(employee)
        db.commit()

        logger.info(
            "Employee deleted successfully. ID: %s",
            employee_id
        )

        return True

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Database error while deleting employee")
        raise


# 6. Filter employees by department
def get_employees_by_department(db: Session, department: str):

    query = select(Employee).where(
        func.lower(Employee.department) == department.lower()
    )

    return db.scalars(query).all()


# 7. Employees with rating at least 4
def get_high_performers(db: Session):

    query = (
        select(Employee)
        .where(Employee.performance_rating >= 4)
        .order_by(Employee.performance_rating.desc())
    )

    return db.scalars(query).all()


# 8. Average performance rating by department
def get_department_average(db: Session):

    query = (
        select(
            Employee.department,
            func.avg(Employee.performance_rating).label(
                "average_rating"
            )
        )
        .group_by(Employee.department)
        .order_by(Employee.department)
    )

    results = db.execute(query).all()

    return [
        {
            "department": row.department,
            "average_rating": round(float(row.average_rating), 2)
        }
        for row in results
    ]


# 9. Five highest-rated employees
def get_top_five_employees(db: Session):

    query = (
        select(Employee)
        .order_by(
            Employee.performance_rating.desc(),
            Employee.employee_id.asc()
        )
        .limit(5)
    )

    return db.scalars(query).all()


# 10. Classify employee performance
def classify_employee(db: Session):

    query = select(Employee).order_by(Employee.employee_id)

    employees = db.scalars(query).all()

    result = []

    for employee in employees:

        if employee.performance_rating >= 4.5:
            category = "Outstanding"

        elif employee.performance_rating >= 3.5:
            category = "Good"

        else:
            category = "Needs Improvement"

        employee_data = {
            "employee_id": employee.employee_id,
            "employee_name": employee.employee_name,
            "department": employee.department,
            "designation": employee.designation,
            "salary": employee.salary,
            "performance_rating": employee.performance_rating,
            "projects_completed": employee.projects_completed,
            "attendance_percentage": employee.attendance_percentage,
            "review_year": employee.review_year,
            "performance_category": category
        }

        result.append(employee_data)

    return result
