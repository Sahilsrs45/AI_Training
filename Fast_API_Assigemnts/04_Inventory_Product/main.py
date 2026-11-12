
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from services import inventoryproduct_service as Service
from schemas.inventoryproduct_schema import (
    ProductCreate,
    ProductResponse,ProductUpdate
)
from config.database import Base, engine, get_db


app = FastAPI(
    title="Inventory and Product Management API",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to Inventory and Product Management API"}

#1 add product
@app.post("/products", response_model=ProductResponse)
def add_product(product: ProductCreate):
    db = SessionLocal()

    try:
        new_product = Service.add_product(db, product)
        return new_product

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Product already exists"
        )

    finally:
        db.close()

#2 get all product
@app.get("/products", response_model=list[ProductResponse])
def get_all_products(skip: int = 0, limit: int = 10):
    db = SessionLocal()

    try:
        products = Service.get_all_products(db, skip, limit)
        return products

    finally:
        db.close()

#3 get product by id
@app.get("/product/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    db = SessionLocal()

    try:
        product = Service.get_product_by_id(db, product_id)

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product

    finally:
        db.close()

#5 delete product
@app.delete("/product/{product_id}")
def delete_product(product_id: int):

    db = SessionLocal()

    try:
        result = Service.delete_product(db, product_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return {
            "message": "Product deleted successfully"
        }

    finally:
        db.close()

#5 update product
@app.put("/product/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):

    db = SessionLocal()

    try:
        updateprod = Service.update_product(db, product_id, product)

        if updateprod is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return updateprod

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Product update conflicts with existing data"
        )

    finally:
        db.close()

#6 filter by category
@app.get("/products/category/{category}", response_model=list[ProductResponse])
def get_products_by_category(category: str):

    db = SessionLocal()

    try:
        products = Service.get_products_by_category(db, category)
        return products

    finally:
        db.close()
#7 low stock product
@app.get("/products/low-stock", response_model=list[ProductResponse])
def get_low_stock_products():

    db = SessionLocal()

    try:
        products = Service.get_low_stock_products(db)
        return products

    finally:
        db.close()

#8 increase quantity in stock
@app.patch("/products/{product_id}/increase-stock",response_model=ProductResponse) 
def increase_ProductStock(product_id:int,quantity:int):
    db=SessionLocal()
    try:
        if quantity <= 0:
            raise HTTPException(
                status_code=422,
                detail="Quantity must be greater than zero"
            )

        product = Service.increase_stock(db, product_id, quantity)

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if product is False:
            raise HTTPException(
                status_code=422,
                detail="Invalid stock quantity"
            )

        return product

    finally:
        db.close()
    
#9 decrease stock 
@app.patch("/products/{product_id}/decrease-stock",response_model=ProductResponse)
def decrease_product_stock(product_id:int,quantity:int):
    db=SessionLocal()
    try:
        if quantity <= 0:
                    raise HTTPException(
                        status_code=422,
                        detail="Quantity must be greater than zero"
                    )
        product=Service.decrease_stock(db,product_id,quantity)

        if product is None:
                    raise HTTPException(
                        status_code=404,
                        detail="Product not found"
                    )
        
        if product is False:
                    raise HTTPException(
                        status_code=422,
                        detail="Invalid stock quantity"
                    )
        
        return product
        
    finally:
            db.close()


    




