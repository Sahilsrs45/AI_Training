import pandas as pd
import numpy as np

# ====================================================
# Read CSV File
# ====================================================

payroll_df = pd.read_csv(
    r"D:\Coforge\AI Training\AI_Training\Payroll_Flow_Capstone_Problem_Statement\data\employee_payroll.csv"
)

# ====================================================
# 1. Load CSV and inspect first 10 records
# ====================================================

print("First 10 Records")
print(payroll_df.head(10))

# ====================================================
# 2. Inspect last 10 records
# ====================================================

print("Last 10 Records")
print(payroll_df.tail(10))

# ====================================================
# 3. Inspect shape of dataset
# ====================================================

print("Dataset Shape")
print(payroll_df.shape)

# ====================================================
# 4. Inspect columns and data types
# ====================================================

print("Column Names")
print(payroll_df.columns)

print("Data Types")
print(payroll_df.dtypes)

# ====================================================
# 5. Generate descriptive statistics
# ====================================================

print("Descriptive Statistics")
print(payroll_df.describe(include="all"))

# ====================================================
# 6. Detect missing values
# ====================================================

print("Missing Values")

missing_values = payroll_df.isnull().sum()

print(missing_values)

# ====================================================
# 7. Remove duplicate employee-month rows
# ====================================================

print("Duplicate Records Before Cleaning")

print(
    payroll_df.duplicated(
        subset=["EmployeeID", "PayrollMonth"]
    ).sum()
)

cleaned_payroll_df = payroll_df.drop_duplicates(
    subset=["EmployeeID", "PayrollMonth"],
    keep="first"
)

print("Duplicate Records After Cleaning")

print(
    cleaned_payroll_df.duplicated(
        subset=["EmployeeID", "PayrollMonth"]
    ).sum()
)

# ====================================================
# 8. Impute missing salary and bonus values
# ====================================================

cleaned_payroll_df["BasicSalary"] = pd.to_numeric(
    cleaned_payroll_df["BasicSalary"],
    errors="coerce"
)

salary_median = cleaned_payroll_df.loc[
    cleaned_payroll_df["BasicSalary"] > 0,
    "BasicSalary"
].median()

cleaned_payroll_df["BasicSalary"] = (
    cleaned_payroll_df["BasicSalary"]
    .fillna(salary_median)
)

cleaned_payroll_df["Bonus"] = (
    cleaned_payroll_df["Bonus"]
    .fillna(0)
)

print("Missing Salary Values")

print(
    cleaned_payroll_df["BasicSalary"]
    .isnull()
    .sum()
)

print("Missing Bonus Values")

print(
    cleaned_payroll_df["Bonus"]
    .isnull()
    .sum()
)

# ====================================================
# 9. Standardize department names
# ====================================================

department_mapping = {

    "it": "IT",
    "information technology": "IT",

    "hr": "HR",
    "human resources": "HR",

    "finance": "Finance",
    "fin.": "Finance",

    "sales": "Sales",
    "business development": "Sales",

    "operations": "Operations",
    "operation": "Operations"

}

cleaned_payroll_df["Department"] = (
    cleaned_payroll_df["Department"]
    .astype(str)
    .str.strip()
    .str.lower()
)

cleaned_payroll_df["Department"] = (
    cleaned_payroll_df["Department"]
    .replace(department_mapping)
)

print("Departments After Cleaning")

print(
    cleaned_payroll_df["Department"]
    .unique()
)

# ====================================================
# 10. Standardize city names
# ====================================================

cleaned_payroll_df["City"] = (
    cleaned_payroll_df["City"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("Cities After Cleaning")

print(
    cleaned_payroll_df["City"]
    .unique()
)

# ====================================================
# 11. Convert JoiningDate and PayrollMonth
# ====================================================

cleaned_payroll_df["JoiningDate"] = pd.to_datetime(
    cleaned_payroll_df["JoiningDate"],
    errors="coerce"
)

cleaned_payroll_df["PayrollMonth"] = pd.to_datetime(
    cleaned_payroll_df["PayrollMonth"],
    errors="coerce"
)

print(
    cleaned_payroll_df[
        ["JoiningDate", "PayrollMonth"]
    ].head()
)

# ====================================================
# 12. Filter employees with salary > 75000
# ====================================================

high_salary_df = cleaned_payroll_df[
    cleaned_payroll_df["BasicSalary"] > 75000
]

print("Employees Earning More Than 75000")

print(high_salary_df.head())

# ====================================================
# 13. Sort employees by salary descending
# ====================================================

salary_sorted_df = cleaned_payroll_df.sort_values(
    by="BasicSalary",
    ascending=False
)

print("Top Salary Records")

print(salary_sorted_df.head(10))

# ====================================================
# 14. Create Gross Salary Column
# ====================================================

cleaned_payroll_df["GrossSalary"] = (

    cleaned_payroll_df["BasicSalary"]

    +

    cleaned_payroll_df["HRA"]

    +

    cleaned_payroll_df["Bonus"]

)

print(
    cleaned_payroll_df[
        [
            "BasicSalary",
            "HRA",
            "Bonus",
            "GrossSalary"
        ]
    ].head()
)

# ====================================================
# 15. Create Net Salary Column
# ====================================================

cleaned_payroll_df["NetSalary"] = (

    cleaned_payroll_df["GrossSalary"]

    -

    cleaned_payroll_df["Deductions"]

)

print(
    cleaned_payroll_df[
        [
            "GrossSalary",
            "Deductions",
            "NetSalary"
        ]
    ].head()
)

# ====================================================
# 16. Calculate attendance percentage
# ====================================================

cleaned_payroll_df["AttendancePercentage"] = (

    cleaned_payroll_df["PresentDays"]

    /

    cleaned_payroll_df["WorkingDays"]

) * 100

print(
    cleaned_payroll_df[
        [
            "PresentDays",
            "WorkingDays",
            "AttendancePercentage"
        ]
    ].head()
)

# ====================================================
# 17. Categorize salaries using np.where
# ====================================================

cleaned_payroll_df["SalaryCategory"] = np.where(

    cleaned_payroll_df["NetSalary"] >= 100000,

    "High Salary",

    "Normal Salary"

)

print(
    cleaned_payroll_df[
        [
            "NetSalary",
            "SalaryCategory"
        ]
    ].head()
)

# ====================================================
# 18. Group by department and calculate average salary
# ====================================================

department_average_salary = (

    cleaned_payroll_df

    .groupby("Department")["NetSalary"]

    .mean()

)

print("Department Wise Average Salary")

print(department_average_salary)

# ====================================================
# 19. Top 10 highest paid employees
# ====================================================

top_10_employees = cleaned_payroll_df.nlargest(
    10,
    "NetSalary"
)

print("Top 10 Highest Paid Employees")

print(
    top_10_employees[
        [
            "EmployeeID",
            "EmployeeName",
            "Department",
            "NetSalary"
        ]
    ]
)

# ====================================================
# 20. Create Pivot Table and Export Cleaned CSV
# ====================================================

pivot_table = pd.pivot_table(

    cleaned_payroll_df,

    values="NetSalary",

    index="Department",

    aggfunc="sum"

)

print("Department Wise Total Payroll")

print(pivot_table)

cleaned_payroll_df.to_csv(
    "cleaned_employee_payroll.csv",
    index=False
)

print("Cleaned Payroll File Exported Successfully")