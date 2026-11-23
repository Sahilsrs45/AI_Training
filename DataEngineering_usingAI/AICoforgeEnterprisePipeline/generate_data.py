import pandas as pd
import random
from pathlib import Path
random.seed(42)
departments = [
   "IT", "HR", "Finance",
   "Sales", "Operations"
]
cities = [
   "Pune", "Delhi", "Mumbai",
   "Chennai", "Bangalore"
]
folder = Path("data/employees")
folder.mkdir(parents=True, exist_ok=True)
emp_id = 1
for department in departments:
   employees = []
   for i in range(200):
       employee = {
           "emp_id": emp_id,
           "emp_name": f"Employee_{emp_id}",
           "department": department,
           "salary": random.randint(25000, 150000),
           "city": random.choice(cities)
       }
       employees.append(employee)
       emp_id += 1
   df = pd.DataFrame(employees)
   filename = folder / f"{department.lower()}_employees.csv"
   df.to_csv(filename, index=False)
   print(f"Created: {filename}")