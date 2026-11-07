from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent

print(f"Base directory :{BASE_DIR}")

DATA_DIR=BASE_DIR/"data"
REPORT_DIR=BASE_DIR/"report"
DATABASE_DIR=BASE_DIR/"database"

print(f"Data directory :{DATA_DIR}")
print(f"Report directory :{REPORT_DIR}")
print(f"Database directory : {DATABASE_DIR}")

DATABASE_PATH=DATABASE_DIR/"ecommerce_warehouse.db"
#
def create_folder()->None:
    """Create  report and database folders if they do not exist"""
    
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)