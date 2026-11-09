from decimal import Decimal
from sqlalchemy.orm import Session
from models.employeeperformance_model import Employee
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select,func

#add employee
def add_employee(db:Session,data):
    Employee=Employee(**data.model_dump())
    db.add(Employee)
    db.commit()
    db.refresh(Employee)
    return Employee
#get all employees

def get_all_employees(db:Session):
    query=select(Employee).order_by(Employee.EmployeeId)
    result=db.scalars(query)
    
    
#get employee by id
def get_employee_byId(db:Session,EmployeeId:int):
    
    return db.get(Employee,EmployeeId)
     
#delete employee
def deleteEmployee(db:Session,EmployeeId:int):
    Employee=db.get(Employee,EmployeeId)
    if Employee is None:
        return False
    
    db.delete(Employee)
    db.commit()
    return True

#update Employee
def update_Employee(db:Session,data,EmployeeId:int):
    Employee=db.get(Employee,EmployeeId)
    if Employee is None:
        return False
    
    for key,value in data.model_deump().items():
        setattr(Employee,key,value)
        try:
            db.commit()
            db.refresh(Employee)
            return Employee
        except IntegrityError:
            db.rollback()
            raise
    