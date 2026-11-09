from sqlalchemy import(Column,Integer,String,Numeric,Float)
from config.database import Base

class Employee(Base):
    ___tablename___="Employees"
    
    EmployeeId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    EmployeeName = Column(String(100), nullable=False)
    Department = Column(String(50), nullable=False)
    Designation = Column(String(100), nullable=False)
    Salary = Column(Numeric(10, 2), nullable=False)
    PerformanceRating = Column(Float, nullable=False)
    ProjectsCompleted = Column(Integer, nullable=False)
    AttendancePercentage = Column(Float, nullable=False)
    ReviewYear = Column(Integer, nullable=False)
    
    

