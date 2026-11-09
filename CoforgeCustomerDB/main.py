from fastapi import FastAPI
from services import customer_service as service
from schemas.customer_schema import CustomerCreate,CustomerResponse
from config.database import SessionLocal,engine,Base
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from config.logging import logger
 
app=FastAPI(
    title="Customer Management API",
    version='1.0.1'
)
Base.metadata.create_all(bind=engine)
 
@app.get("/")
def home():
    return{
        "message":"Welcome to Customer Management API"
    }
 
# get all customer
@app.get("/customers",response_model=list[CustomerResponse])
def getAllCustomer():
    logger.info("GetAllCustomers API called")
    db=SessionLocal()
 
    try:
        customers=service.get_all_customers(db)
        logger.info(f"Succesfully retrieved %s customers {len(customers)}",)
        return customers
    finally:
        db.close()
 
# get customers by id
@app.get("/customers/{CustomerID}",response_model=CustomerResponse)
def getCustomerById(CustomerId: int):
    logger.info("GetAllCustomers API called")
 
    db=SessionLocal()
    return service.customer_by_id(db,CustomerId)
 
# create customer
@app.post("/customers",response_model=CustomerResponse,status_code=201)
def addCustomer(Customer: CustomerCreate):
    db=SessionLocal()
 
    try:
        new_customer=service.add_customer(db,Customer)
        return new_customer
 
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Customer already exists")
 
    finally:
        db.close()
        
# Update Customer
@app.put("/customers/{CustomerId}", response_model=CustomerResponse)
def updateCustomer(CustomerId: int, Customer: CustomerCreate):
    db = SessionLocal()

    try:
        updated_customer = service.update_customer(
            db,
            CustomerId,
            Customer
        )

        if updated_customer is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return updated_customer

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Customer email already exists"
        )

    finally:
        db.close()
        
        
# Delete Customer
@app.delete("/customers/{CustomerId}")
def deleteCustomer(CustomerId: int):
    db = SessionLocal()

    try:
        deleted = service.delete_customer(
            db,
            CustomerId
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return {
            "message": f"Customer {CustomerId} deleted successfully"
        }

    finally:
        db.close()                