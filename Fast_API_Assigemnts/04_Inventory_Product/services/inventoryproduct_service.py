from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.inventoryproduct_model import Product


# 1. Add Product
def add_product(db: Session, data):

    try:
        product = Product(**data.model_dump())

        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    except SQLAlchemyError:
        db.rollback()
        raise


# 2. Get All Products with Pagination
def get_all_products(db: Session, skip: int = 0, limit: int = 10):

    products = (
        db.query(Product)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return products

#3 get product  by id
def get_product_by_id(db:Session,product_id:int):
    return db.get(Product,product_id)



# 4. Delete Product
def delete_product(db: Session, product_id: int):

    try:
        product = db.get(Product, product_id)

        if product is None:
            return False

        db.delete(product)
        db.commit()

        return True

    except SQLAlchemyError:
        db.rollback()
        raise

#5 update product
def update_product(db: Session, product_id: int, data):

    try:
        product = db.get(Product, product_id)

        if product is None:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)

        return product

    except SQLAlchemyError:
        db.rollback()
        raise

#6 filter by category

def get_products_by_category(db: Session, category: str):

    query = select(Product).where(
        Product.category == category
    )

    products = db.execute(query).scalars().all()

    return products

#7 low stock product
def get_low_stock_products(db: Session):
    query=select(Product).where(
        Product.quantity_in_stock<=Product.reorder_level
    )
    products=db.execute(query).scalars().all()

    return products                

#8 increase the stock
def increase_stock(db:Session,product_id:int,quantity:int):
    try:
        product=db.get(Product,product_id)

        if product is None:
            return None
        if quantity <=0:
            return False

        product.quantity_in_stock+=quantity


        db.commit()
        db.refresh(product)
        return product
    except SQLAlchemyError:
        db.rollback()
        raise    

#9 decrease stock

# 9. Decrease Stock
def decrease_stock(db: Session, product_id: int, quantity: int):

    try:
        product = db.get(Product, product_id)

        if product is None:
            return None

        if quantity <= 0:
            return False

        if product.quantity_in_stock < quantity:
            return False

        product.quantity_in_stock -= quantity

        db.commit()
        db.refresh(product)

        return product

    except SQLAlchemyError:
        db.rollback()
        raise



        


        
    
