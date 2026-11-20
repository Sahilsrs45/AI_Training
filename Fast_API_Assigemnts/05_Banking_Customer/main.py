from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import (
    Base,
    engine,
    SessionLocal
)

from schemas.bankcustomer_schema import (
    CustomerCreate,
    CustomerUpdate,
    TransactionRequest
)

from services.bankcustomer_service import *

app = FastAPI(
    title="Banking Customer Account API"
)

Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.post("/accounts")
def create_customer(
        request: CustomerCreate,
        db: Session = Depends(get_db)
):

    return create_account(
        request,
        db
    )


@app.get("/accounts")
def get_customers(
        page: int = 1,
        size: int = 5,
        db: Session = Depends(get_db)
):

    return get_all_accounts(
        page,
        size,
        db
    )


@app.get("/accounts/{account_number}")
def get_customer(
        account_number: str,
        db: Session = Depends(get_db)
):

    return get_account_by_number(
        account_number,
        db
    )


@app.put("/accounts/{account_number}")
def update_customer(
        account_number: str,
        request: CustomerUpdate,
        db: Session = Depends(get_db)
):

    return update_account(
        account_number,
        request,
        db
    )


@app.delete("/accounts/{account_number}")
def delete_customer(
        account_number: str,
        db: Session = Depends(get_db)
):

    return close_account(
        account_number,
        db
    )


@app.get("/branch/{branch_name}")
def filter_branch(
        branch_name: str,
        db: Session = Depends(get_db)
):

    return get_by_branch(
        branch_name,
        db
    )


@app.get("/account-type/{account_type}")
def filter_account_type(
        account_type: str,
        db: Session = Depends(get_db)
):

    return get_by_account_type(
        account_type,
        db
    )


@app.post("/deposit/{account_number}")
def deposit(
        account_number: str,
        request: TransactionRequest,
        db: Session = Depends(get_db)
):

    return deposit_amount(
        account_number,
        request.amount,
        db
    )


@app.post("/withdraw/{account_number}")
def withdraw(
        account_number: str,
        request: TransactionRequest,
        db: Session = Depends(get_db)
):

    return withdraw_amount(
        account_number,
        request.amount,
        db
    )


@app.get("/branch-total")
def get_branch_total(
        db: Session = Depends(get_db)
):

    return total_branch_deposit(db)