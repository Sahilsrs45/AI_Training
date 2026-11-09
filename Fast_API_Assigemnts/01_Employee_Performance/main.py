from fastapi import FastAPI, HTTPException
from services import employeeperformance_service as Service
from schemas.employeeperformance_schema import EmployeeCreate, EMployeeResponse, EmployeeUpdate
from config.database import SessionLocal, engine, Base
from sqlalchemy.exc import IntegrityError

app = FastAPI(
    title="Employee Performance API",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

# Get all employees
@app.get("/employee", response_model=list[EMployeeResponse])
def get_all_employees():
    db = SessionLocal()

    try:
        employees = Service.get_all_employees(db)
        return employees
    finally:
        db.close()
        
        
#get employee by id
@app.get("/employee/{EmployeeId}",response_model=EMployeeResponse)
def get_employee_byId(EmployeeId:int):
    db=SessionLocal()
    return Service.get_employee_byId(EmployeeId,db)

#add employee
@app.post("/employee/{EmployeeId}" ,response_model=EMployeeResponse)
def add_employee(Employee:EmployeeCreate,status_code=201):
    db=SessionLocal()
    try:
        new_employee=Service.add_employee(db,Employee)
        return new_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,details="employee already exist")
    finally:db.close()        
    
#update
@app.put("/employees/{EmployeeId}",response_model=EMployeeResponse)
def update_employee(EmployeeId:int,Employee:EmployeeCreate):
    db=SessionLocal()
    try:
        updated_employee=Service.update_Employee(db,EmployeeId,Employee)
        if updated_employee is None:
            raise HTTPException(status_code=404,detail="not found")
        return updated_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,details="already exists")
    finally:
        db.close()
            
            
#delete
@app.delete("/employee/{EmployeeId}")
def delete_employee(EmployeeId:int):
    db=SessionLocal()
    try:
        delete_employee=Service.deleteEmployee(db,EmployeeId)
        if not delete_employee:
            raise HTTPException(
                status_cod=404,
                detail="employee not found"
                
            )
        return{"message ":"deleted_successfully"}
    finally:
        db.close()    
            