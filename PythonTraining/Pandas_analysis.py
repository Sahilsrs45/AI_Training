
import pandas as pd
#import numpy as np

salary_series=pd.Series([
    65000,58000,72000,80000,85000,68000,90000,76000
])

print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)


employee_series=pd.Series(
    [
        "Shiv","sahil","atharva","prince","shreyansh","hitesh","akashdeep","pranjali"
    ],
    index=["E101","E102","E103","E104","E105","E106","E107","E108"]
    
)

print(employee_series)

#retrieve employees
print("Employee Name with E103")
print(employee_series["E103"])

print("Employee Name with E106")
print(employee_series["E106"])
employee_data ={
    "Employee_ID":["E101","E102","E103","E104","E105","E106","E107","E108"],
    "Employee_Name": [
            "Shiv","sahil","atharva","prince","shreyansh","hitesh","akashdeep","pranjali"
        ],
    "Department":["Sales","HR","Sales","Finance","IT","Sales","IT","Finance"],
    "City": ["Delhi","Mumbai","Pune","Delhi","Mumbai","Bengaluru","Pune","Delhi"],
    "Salary":[65000,58000,72000,80000,85000,68000,90000,76000],
    "Experience":[5,4,7,8,6,5,9,6],
    "Rating":[4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3]
}

print("Create Employee dataframe")
employees_df=pd.DataFrame(employee_data)
print(employees_df)

print(employees_df.shape)
print(employees_df.columns)
print(employees_df.dtypes)

print(employees_df.head())
print(employees_df.head(2))
print(employees_df.tail())
print(employees_df.tail(2))


print(employees_df["Employee_Name"])
print(employees_df[["Employee_Name","Salary"]])

result=employees_df[employees_df["Salary"]>80000]
print(result)

performance=employees_df[employees_df["Rating"]>4.5]
print(performance)

emp_dept_sales_result=employees_df[employees_df["Department"]=="Sales"]
print(emp_dept_sales_result)
emp_city_delhi_result=employees_df[employees_df["City"]=="Delhi"]
print(emp_city_delhi_result)

emp_rating_salary_result=employees_df[(employees_df["Rating"]>=4.5) & (employees_df["Salary"]>=70000)]
print(emp_rating_salary_result)

emp_dept_IT_Finance_result=employees_df[(employees_df["Department"]=="IT") | (employees_df["Department"]=="Finance")]
print(emp_dept_IT_Finance_result)

emp_dept_IT_Finance_result_isin=employees_df[employees_df["Department"].isin(["IT","Finance"])]
print(emp_dept_IT_Finance_result_isin)
employees_df["AnnualSalary"]=employees_df["Salary"]*12
print(employees_df)


employees_df["IncrementSalary"]=employees_df["Salary"]+employees_df["Salary"]*0.08
print(employees_df)
employees_df["Bonus"]=employees_df["IncrementSalary"]*0.05
print(employees_df)

employees_df["Monthly_Compensation"]=employees_df["Bonus"]+employees_df["IncrementSalary"]

print(employees_df)

min_salary=employees_df["Salary"].min()
print(min_salary)

max_salary=employees_df["Salary"].max()
print(max_salary)
mean_salary=employees_df["Salary"].mean()
print(mean_salary)

total_salary=employees_df["Salary"].sum()
print(total_salary)

average_rating=employees_df["Rating"].mean()
print("Average rating : ",average_rating)
dept_count=employees_df["Department"].value_counts()
print(dept_count)

dept_len=len(employees_df["Department"].value_counts())
print(dept_len)

dep_unique=employees_df["Department"].nunique()

print(dep_unique)
#according to ascending order
emp_salary_sort=employees_df.sort_values(by="Salary")

print(emp_salary_sort)

emp_salary_sortdesc=employees_df.sort_values(by="Salary", ascending=False)
print(emp_salary_sortdesc)

emp_salary_topthree=employees_df.sort_values(by="Salary", ascending=False).head(3)
print(emp_salary_topthree)

