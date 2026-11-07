#to use variables os is used
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy.engine import URL

load_dotenv()
class Base(DeclarativeBase):
    pass

database_url=URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT","3306")),
    database=os.getenv("DB_NAME","EMmployeeDB")
)

engine=create_engine(
    database_url
)

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
)
def get_db():
    db=SessionLocal()
    try:
        yield db
        
    finally:
        db.close()    