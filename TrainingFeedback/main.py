from fastapi import FastAPI
from schemas.employee_schema import EmployeeResponse,EmployeeUpdate,EmployeeCreate
from services import employee_service as Service
from config.database import Base, engine, SessionLocal


app=FastAPI(
    title="API IS running",
    version="1.0.1"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def Home():
    return {"Fast Api is working"
    }
    
@app.get("/employees",response_model=list[EmployeeResponse])    
def getAllEmployee():
    db=SessionLocal()
    return Service.get_all_employees(db)
    
    
@app.get("/employees/{employee_id}",response_model=EmployeeResponse)
def get_Employee_by_Id(employee_id:int):
    db=SessionLocal()
    return Service.get_employee_by_id(db,employee_id)   


@app.post("/employee/add",response_model=EmployeeResponse)

def addEmployee(employee:EmployeeCreate):
    db=SessionLocal()
    return Service.add_employee(db,employee)

 

@app.delete("/employees/delete/{employee_id}",response_model=EmployeeResponse)
def delete_Employee(employee_id:int):
    
    db=SessionLocal()
    return Service.delete_employee(db,employee_id)

# @app.put("/employees/update/{employee_id}")