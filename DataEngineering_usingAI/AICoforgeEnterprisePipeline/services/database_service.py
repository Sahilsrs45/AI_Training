from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config.settings import (
    MYSQL_DB,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_USER
)
 
database_url = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=3306,
    database=MYSQL_DB
)
 
engine = create_engine(
    database_url,
    
)
 
 
def get_database_engine():
    return engine
 