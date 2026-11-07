from sqlalchemy import (Column, Integer, String, Numeric)
from config.database import Base
 
class Employee(Base):
    __tablename__ = "Employees"
 
    employee_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    employee_name = Column(
        String(100),
        nullable=False
    )
    age = Column(
        Integer,
        nullable=False
    )
    email = Column(
        String(150),
        unique=True,
        nullable=False
    )
    department = Column(
        String(100), nullable=False
    )
    designation = Column(
        String(100), nullable=False
    )
    salary = Column(
        Numeric(12,2), nullable=False
    )
    city = Column(
        String(100), nullable=False
    )