from decimal import Decimal
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
 
from models.employee_model import Employee
 
# 1. Add employee
from sqlalchemy.orm import Session
from models.employee_model import Employee
def add_employee(db: Session, data):
    employee = Employee(**data.model_dump())
 
 
    db.add(employee)
 
    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise
 
#2. Display all employees
def get_all_employees(db: Session):
    return db.scalars(
        select(Employee).order_by(Employee.employee_id)
    ).all()
 
#3. Search employee byID
def get_employee_by_id(db: Session, employee_id: int):
    return db.get(Employee,employee_id)
 
#4. Update employee
def update_employee(db:Session, employee_id: int, data):
    employee = db.get(Employee, employee_id)
 
    if employee is None:
        return None
    for key, value in data.model_dump().items():
        setattr(employee, key, value)
 
    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise
#5 Delete Employee
def delete_employee(db:Session,employee_id:int):
    employee=db.get(Employee,employee_id)
    
    if employee is None:
        return False
    
    db.delete(employee)
    db.commit()
    
    return True