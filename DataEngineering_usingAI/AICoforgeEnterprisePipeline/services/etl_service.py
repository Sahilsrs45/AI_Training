from pathlib import Path
import pandas as pd
from sqlalchemy import text
from services.database_service import get_database_engine
def extract_employees():
   folder = Path("data/employees")
   files = sorted(folder.glob("*.csv"))
   if not files:
       raise ValueError("No employee CSV files found")
   dataframes = []
   for file in files:
       df = pd.read_csv(file)
       dataframes.append(df)
   employees = pd.concat(
       dataframes,
       ignore_index=True
   )
   return employees

def transform_employees(df):
   required_columns = [
       "emp_id",
       "emp_name",
       "department",
       "salary",
       "city"
   ]
   missing_columns = [
       column for column in required_columns
       if column not in df.columns
   ]
   if missing_columns:
       raise ValueError(
           f"Missing columns: {missing_columns}"
       )
   df = df.copy()
   df["emp_id"] = pd.to_numeric(
       df["emp_id"],
       errors="coerce"
   )
   df["salary"] = pd.to_numeric(df["salary"],
       errors="coerce"
   )
   for column in ["emp_name", "department", "city"]:
       df[column] = df[column].astype("string").str.strip()
   df["department"] = df["department"].str.upper()
   valid = (
       df["emp_id"].notna()
& (df["emp_id"] > 0)
& (df["emp_id"] % 1 == 0)
& df["salary"].notna()
& (df["salary"] > 0)
& df["emp_name"].notna()
& (df["emp_name"] != "")
& df["department"].notna()
& (df["department"] != "")
& df["city"].notna()
& (df["city"] != "")
   )
   rejected = df.loc[~valid].copy()
   cleaned = df.loc[valid].copy()
   cleaned["emp_id"] = cleaned["emp_id"].astype(int)
   cleaned = cleaned.drop_duplicates(
       subset=["emp_id"],
       keep="last"
   )
   return cleaned, rejected

def load_employees(df):
   engine = get_database_engine()
   statement = text("""
       INSERT INTO employees
       (emp_id, emp_name, department, salary, city)
       VALUES
       (:emp_id, :emp_name, :department, :salary, :city)
       ON DUPLICATE KEY UPDATE
           emp_name = VALUES(emp_name),
           department = VALUES(department),
           salary = VALUES(salary),
           city = VALUES(city)
   """)
   records = df.to_dict(orient="records")
   with engine.begin() as connection:
       if records:
           connection.execute(statement, records)
   return len(records)

def run_etl():
   original = extract_employees()
   cleaned, rejected = transform_employees(original)
   Path("logs").mkdir(exist_ok=True)
   rejected.to_csv(
       "logs/rejected_employees.csv",
       index=False
   )
   processed = load_employees(cleaned)
   return {
       "status": "success",
       "input_records": len(original),
       "valid_records": len(cleaned),
       "rejected_records": len(rejected),
       "processed_records": processed
   }

def department_summary():
   engine = get_database_engine()
   query = text("""
       SELECT
           department,
           COUNT(*) AS employee_count,
           SUM(salary) AS total_salary,
           AVG(salary) AS average_salary
       FROM employees
       GROUP BY department
       ORDER BY department
   """)
   with engine.connect() as connection:
       rows = connection.execute(query).mappings().all()
   return [
       {
           "department": row["department"],
           "employee_count": row["employee_count"],
           "total_salary": float(row["total_salary"]),
           "average_salary": float(row["average_salary"])
       }
       for row in rows
   ]