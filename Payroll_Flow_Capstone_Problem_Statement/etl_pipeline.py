
import pandas as pd
from pathlib import Path

#reading the file
payroll_df=pd.read_csv(r"D:\Coforge\AI Training\AI_Training\Payroll_Flow_Capstone_Problem_Statement\data\employee_payroll.csv")

#1. Load CSV and inspect first/last 10 records
print(payroll_df.head(10))

print(payroll_df.tail(10))


#2. Inspect shape, columns, and dtypes
print("Shape",payroll_df.shape)
print("columns",payroll_df.columns)
print("data type",payroll_df.dtypes)

#3. Generate descriptive statistics
print(payroll_df.describe())

#4. Detect missing values
missing_value=payroll_df.isnull().sum()
print(missing_value)

#5. Remove duplicate employee-month rows
print("Before removing duplicates",payroll_df.duplicated(
     subset=["EmployeeID","PayrollMonth"]

).sum())

cleaned_payroll_df=payroll_df.drop_duplicates(
   subset=["EmployeeID","PayrollMonth"],keep="first"
)

print(cleaned_payroll_df)

print("After removing duplicates ",cleaned_payroll_df.duplicated(
    subset=["EmployeeID","PayrollMonth"]).sum()
)

#6. Impute missing salary and bonus values using documented rules
# Calculate median using valid positive salaries

cleaned_payroll_df["BasicSalary"] = pd.to_numeric(
    cleaned_payroll_df["BasicSalary"],
    errors="coerce"
)

salary_median = cleaned_payroll_df["BasicSalary"].median()

cleaned_payroll_df["BasicSalary"] = (
    cleaned_payroll_df["BasicSalary"].fillna(salary_median)
)

print("Missing Salary:",
      cleaned_payroll_df["BasicSalary"].isnull().sum())

#7. Standardize department and city names

print("Unique Departments:")
print(cleaned_payroll_df["Department"].unique())

department_mapping = {
    "it": "IT",
    " IT ": "IT",
    "Information Technology": "IT",
    "hr": "HR",
    " HR ": "HR",
    "Human Resources": "HR",
    "FINANCE": "Finance",
    " finance ": "Finance",
    "Fin.": "Finance",
    "sales": "Sales",
    " SALES ": "Sales",
    "Business Development": "Sales",
    "operations": "Operations",
    " OPS ": "Operations",
    "Operation": "Operations"
}

cleaned_payroll_df["Department"] = (
    cleaned_payroll_df["Department"].replace(department_mapping)
)

city_mapping = {
    " pune ": "Pune",
    "MUMBAI": "Mumbai",
    "Bangalore": "Bengaluru",
    "HYD": "Hyderabad",
    "chennai": "Chennai",
    " NOIDA ": "Noida"
}

cleaned_payroll_df["City"] = (
    cleaned_payroll_df["City"].replace(city_mapping)
)

#8. Convert joining and payroll dates
cleaned_payroll_df["JoiningDate"]=pd.to_datetime(
    cleaned_payroll_df["JoiningDate"],errors="coerce"
)

cleaned_payroll_df["PayrollMonth"]=pd.to_datetime(
    cleaned_payroll_df["PayrollMonth"],errors="coerce"
)

#9. Filter salaries above ₹75,000
salary_above=cleaned_payroll_df[
    cleaned_payroll_df["BasicSalary"]>75000
]
print("Salaries above 75000:\n ",salary_above)

#10. Sort by salary
sort_by_salary=cleaned_payroll_df.sort_values(
    by="BasicSalary",ascending=False
)
print(sort_by_salary)
#11. Calculate gross salary (BasicSalary + HRA + Bonus)
cleaned_payroll_df["gross_salary"] = (
    cleaned_payroll_df["BasicSalary"]
    + cleaned_payroll_df["HRA"]
    + cleaned_payroll_df["Bonus"]
)

print(cleaned_payroll_df[["BasicSalary", "HRA", "Bonus", "gross_salary"]])
#12. Calculate net salary (GrossSalary − Deductions)
cleaned_payroll_df["NetSalary"]=(cleaned_payroll_df["gross_salary"]-cleaned_payroll_df["Deductions"])
print("Net salary: ",cleaned_payroll_df)
#13. Calculate attendance percentage

cleaned_payroll_df["attendance_percentage"] = (
    cleaned_payroll_df["PresentDays"] /
    cleaned_payroll_df["WorkingDays"]
) * 100


#14. Categorize salaries using np.where or np.select
import numpy as np

cleaned_payroll_df["salary_category"] = np.where(
    cleaned_payroll_df["BasicSalary"] > 75000,
    "High Salary",
    "Other"
)






conditions = [
    cleaned_payroll_df["BasicSalary"] < 40000,
    (cleaned_payroll_df["BasicSalary"] >= 40000) &
    (cleaned_payroll_df["BasicSalary"] <= 75000),
    cleaned_payroll_df["BasicSalary"] > 75000
]

choices = ["Low Salary", "Medium Salary", "High Salary"]

cleaned_payroll_df["SalaryCategory"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

print(cleaned_payroll_df[
    ["EmployeeID", "BasicSalary", "SalaryCategory"]
].head(10))

print(cleaned_payroll_df[
    ["EmployeeID", "BasicSalary", "SalaryCategory"]
].head(10))

#15. Group by department
group_by_dept=cleaned_payroll_df.groupby("Department")["EmployeeID"].count()
print(group_by_dept)

#16. Calculate department-wise average salary
department_wise_avg=cleaned_payroll_df.groupby("Department")["BasicSalary"].mean()
print(department_wise_avg)
#17. Identify top 10 highest-paid employees
highest_paid_employee=cleaned_payroll_df.sort_values(by="BasicSalary",ascending=False).head(10)
#18. Build department-wise payroll pivot table
department_payroll_pivot = pd.pivot_table(
    cleaned_payroll_df,
    index="Department",
    values="BasicSalary",
    aggfunc="sum"
)

print(department_payroll_pivot)
#19. Validate negative salaries, attendance limits and IDs


#20. Export cleaned/transformed CSV


# Create output folder
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# Export transformed DataFrame to CSV
cleaned_payroll_df.to_csv(
    output_dir / "cleaned_payroll.csv",
    index=False
)

print("Cleaned and transformed CSV exported successfully!")


