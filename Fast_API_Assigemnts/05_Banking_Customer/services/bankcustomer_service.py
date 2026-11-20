from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from models.bankcustomer_model import BankCustomer


def create_account(request, db: Session):

    existing_customer = db.query(BankCustomer).filter(
        (BankCustomer.email == request.email)
        |
        (BankCustomer.account_number == request.account_number)
    ).first()

    if existing_customer:
        raise HTTPException(
            status_code=409,
            detail="Email or Account Number already exists"
        )

    customer = BankCustomer(
        customer_name=request.customer_name,
        email=request.email,
        account_number=request.account_number,
        account_type=request.account_type,
        branch_name=request.branch_name,
        balance=request.balance,
        opened_on=request.opened_on,
        is_active=True
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def get_all_accounts(page: int, size: int, db: Session):

    skip = (page - 1) * size

    return db.query(BankCustomer)\
        .offset(skip)\
        .limit(size)\
        .all()


def get_account_by_number(account_number: str, db: Session):

    customer = db.query(BankCustomer).filter(
        BankCustomer.account_number == account_number
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return customer


def update_account(
        account_number: str,
        request,
        db: Session
):

    customer = get_account_by_number(
        account_number,
        db
    )

    customer.email = request.email
    customer.branch_name = request.branch_name

    db.commit()
    db.refresh(customer)

    return customer


def close_account(account_number: str, db: Session):

    customer = get_account_by_number(
        account_number,
        db
    )

    if customer.balance > 0:
        raise HTTPException(
            status_code=409,
            detail="Balance should be zero"
        )

    customer.is_active = False

    db.commit()

    return {"message": "Account Closed Successfully"}


def get_by_branch(branch_name: str, db: Session):

    return db.query(BankCustomer).filter(
        BankCustomer.branch_name == branch_name
    ).all()


def get_by_account_type(
        account_type: str,
        db: Session
):

    return db.query(BankCustomer).filter(
        BankCustomer.account_type == account_type
    ).all()


def deposit_amount(
        account_number: str,
        amount: float,
        db: Session
):

    customer = get_account_by_number(
        account_number,
        db
    )

    if not customer.is_active:
        raise HTTPException(
            status_code=409,
            detail="Account is inactive"
        )

    customer.balance += amount

    db.commit()

    return {
        "message": "Amount Deposited Successfully",
        "balance": customer.balance
    }


def withdraw_amount(
        account_number: str,
        amount: float,
        db: Session
):

    customer = get_account_by_number(
        account_number,
        db
    )

    if not customer.is_active:
        raise HTTPException(
            status_code=409,
            detail="Account is inactive"
        )

    if customer.balance < amount:
        raise HTTPException(
            status_code=409,
            detail="Insufficient Funds"
        )

    customer.balance -= amount

    db.commit()

    return {
        "message": "Amount Withdrawn Successfully",
        "balance": customer.balance
    }


def total_branch_deposit(db: Session):

    return db.query(
        BankCustomer.branch_name,
        func.sum(BankCustomer.balance).label("total_balance")
    ).group_by(
        BankCustomer.branch_name
    ).all()