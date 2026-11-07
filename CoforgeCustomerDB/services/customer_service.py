from decimal import Decimal
from sqlalchemy.orm import Session
from models.customer_model import Customer
from sqlalchemy import select,func
from sqlalchemy.exc import IntegrityError
 
def add_customer(db: Session, data):
    customer=Customer(**data.model_dump())
 
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
 
def get_all_customers(db: Session):
    query=select(Customer).order_by(Customer.CustomerId)
    result=db.scalars(query)
    customers=result.all()
    return customers
 
# search customer by id:
def customer_by_id(db: Session, CustomerId: int):
    return db.get(Customer, CustomerId)
 
# Update Customer
def update_customer(db: Session, CustomerId: int, data):
    customer=db.get(Customer, CustomerId)
 
    if customer is None:
        return None
 
    for key,value in data.model_dump().items():
        setattr(customer,key,value)
 
    try:
        db.commit()
        db.refresh(customer)
        return customer
    except IntegrityError:
        db.rollback()
        raise
 
# Delete Customer
def delete_customer(db: Session, CustomerId:int):
    customer=db.get(Customer,CustomerId)
 
    if customer is None:
        return False
 
    db.delete(customer)
    db.commit()
    return True