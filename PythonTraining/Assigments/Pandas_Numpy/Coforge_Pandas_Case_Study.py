import pandas as pd
import numpy as np
#1. Load the employee CSV into a DataFrame. 
employee_df=pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\coforge_employees_50.csv")
project_df=pd.read_csv(r"C:\Users\Sahil.Ranawade\Downloads\coforge_projects.csv")
print(employee_df)

#2. Display the first five and last five rows. 
print(employee_df.head())

print(employee_df.tail())

# 3. Show shape, column names and data types.
print("Shape:", employee_df.shape)
print("Columns:",employee_df.columns)

print("Data Types:",employee_df.dtypes)



#4. Run info() and describe() and explain the results.
print("Info",employee_df.info())
print("Describe",employee_df.describe())

#5. Select EmployeeName, Department, Salary and PerformanceRating. 
print(employee_df[["EmployeeName","Department","Salary","PerformanceRating"]])

#6. Calculate minimum, maximum and mean salary. 
print("Min Salary:", employee_df["Salary"].min())
print("Max Salary:", employee_df["Salary"].max())
print("Mean Salary:", employee_df["Salary"].mean())

#7. Calculate total annual salary expenditure. 
print("Total Salary:", employee_df["Salary"].sum())

#8. Identify the youngest and oldest employees. 

youngest=employee_df["Age"].min()
print(youngest)
oldest=employee_df["Age"].max()
print(oldest)
#9. Count employees in each department. 
print(employee_df["Department"].value_counts())

#10. Count employees in each office location. 
print(employee_df["Department"].value_counts())
#11. List unique designations and their counts. 

print(employee_df["Designation"].value_counts())
#12. Filter employees with Salary above INR 1,000,000.
print(employee_df[employee_df["Salary"]>100000]) 

#13. Filter employees with PerformanceRating >= 4.
print(employee_df[employee_df["PerformanceRating"]>=4])

#14. Sort by Salary from highest to lowest. 
print(employee_df.sort_values(by="Salary",ascending=False))

#15. Display the five highest-paid employees. 
print(employee_df.sort_values(by="Salary",ascending=False).head(5))


#16. Find mean salary by department using groupby(). 
salary_mean=employee_df.groupby("Department")["Salary"].mean()
print(salary_mean)
#17. Find minimum and maximum salary by designation. 


min_max_salary=    employee_df.groupby("Designation")["Salary"].agg(["min", "max"])
print(min_max_salary)

#18. Find mean performance rating by location. 
performance=employee_df.groupby("Location")["PerformanceRating"].mean()
print(performance)
#19. Count employees grouped by Department and Gender. 
emp=employee_df.groupby(["Department","Gender"]).size().reset_index(name="Count")
print(emp)

#20. Filter employees with ExperienceYears > 5 and PerformanceRating >= 4. 
empwith_exp_performance= employee_df[
        (employee_df["ExperienceYears"] > 5) &
        (employee_df["PerformanceRating"] >= 4)]

print("Employee details :",empwith_exp_performance)

#21. Use isin() to filter employees from any three selected locations. 

locations = ["Pune", "Noida", "Bengaluru"]
print(employee_df[employee_df["Location"].isin(locations)])

#22. Create SalaryCategory (Low, Medium, High); document your thresholds. 
def salary_category(salary):
    if salary<500000 :
        return "Low"
    elif salary<1000000:
        return "medium"
    else :
        return "high"

employee_df["SalaryCategory"]=employee_df["Salary"].apply(salary_category)    
    
print(employee_df[["EmployeeName","Salary","SalaryCategory"]])
#23. Create PerformanceCategory using clear rating thresholds. 
def performance_category(rating):
    if rating <= 2:
        return "Needs Improvement"
    elif rating == 3:
        return "Good"
    else:
        return "Excellent"

employee_df["PerformanceCategory"] = employee_df["PerformanceRating"].apply(performance_category)
print(employee_df[["EmployeeName","PerformanceRating","PerformanceCategory"]])

#24. Calculate salary per year of experience; handle zero experience safely. 


#25. Calculate total Salary and Bonus by department. 

print(employee_df.groupby("Department")[["Salary", "Bonus"]].sum()
)
#26. Calculate average TrainingHours by department. 
print(employee_df.groupby("Department")["TrainingHours"].mean())

#27. Identify employees with LeaveDays > 15.
print(employee_df[employee_df["LeaveDays"] > 15])

#28. Calculate correlation between Salary and ExperienceYears.
print("Correlation",employee_df["Salary"].corr(employee_df["ExperienceYears"]))

#29. Calculate correlation between TrainingHours and PerformanceRating. 
print(employee_df["TrainingHours"].corr(employee_df["PerformanceRating"]))
#30. Group by Department and Designation; show headcount and mean salary.

print(
    employee_df.groupby(['Department', 'Designation']).agg(
        HeadCount=('EmployeeID', 'count'),
        AverageSalary=('Salary', 'mean')
    )
)

# 31. Use agg() to find count, min, max, mean and median salary by department.
print(employee_df.groupby('Department')['Salary'].agg(['count', 'min', 'max', 'mean', 'median'])
)

# 32. Create a pivot table of average salary by Department and Location.
pivot_table = pd.pivot_table(
    employee_df,
    values='Salary',
    index='Department',
    columns='Location',
    aggfunc='mean'
)
print(pivot_table)


# 33. Create a crosstab of Department and WorkMode.
print(
    pd.crosstab(
        employee_df['Department'],
        employee_df['WorkMode']
    )
)

# 34. Convert JoiningDate to datetime and calculate tenure as of the analysis date.
employee_df['JoiningDate'] = pd.to_datetime(employee_df['JoiningDate']
)

employee_df['TenureYears'] = (
    (pd.Timestamp.today() - employee_df['JoiningDate']).dt.days / 365
)

print(
    employee_df[['EmployeeName', 'TenureYears']]
)

# 35. Inspect nulls and duplicates; report findings and clean only where justified.
print(f"Null Values :{employee_df.isnull().sum()}")

print(f"Duplicate Records:{employee_df.duplicated().sum()}")

# 36. Merge employees with projects using ProjectID.
merged_df = pd.merge(
    employee_df,
    project_df,
    on='ProjectID',
    how='left'
)

print(merged_df)


# 37. Compare inner, left, right and outer joins; explain row-count differences.
inner_join = employee_df.merge(project_df, on='ProjectID', how='inner')
left_join = employee_df.merge(project_df, on='ProjectID', how='left')
right_join = employee_df.merge(project_df, on='ProjectID', how='right')
outer_join = employee_df.merge(project_df, on='ProjectID', how='outer')

print("Inner Join Rows:", len(inner_join))
print("Left Join Rows:", len(left_join))
print("Right Join Rows:", len(right_join))
print("Outer Join Rows:", len(outer_join))

# 38. Find employees on projects with ProjectBudgetINR > 10,000,000.
print(
    merged_df[
        merged_df['ProjectBudgetINR'] > 10000000
    ]
)

# 39. Rank employees by Salary within each department.
employee_df['DepartmentSalaryRank'] = (
    employee_df.groupby('Department')['Salary']
    .rank(method='dense', ascending=False)
)

print(
    employee_df[
        ['EmployeeName',
         'Department',
         'DepartmentSalaryRank']
    ]
)

print("-------------------------")

# 40. Find the top three highest-paid employees per department.

top_three = (
    employee_df
    .sort_values('Salary', ascending=False)
    .groupby('Department')
    .head(3)
)

print(f"Top 3 highest paid employees are:\n{top_three}")

# 41. Use transform() to compute Salary minus department mean Salary.
employee_df['SalaryDifference'] = (
    employee_df['Salary'] - employee_df.groupby('Department')['Salary']
    .transform('mean')
)

print(
    employee_df[
        ['EmployeeName',
         'Department',
         'SalaryDifference']
    ]
)

# 42. Calculate the 25th, 50th, 75th and 90th Salary percentiles.
print(
    employee_df['Salary']
    .quantile([0.25, 0.50, 0.75, 0.90])
)

# 43. Detect Salary outliers using the interquartile range (IQR) method.
Q1 = employee_df['Salary'].quantile(0.25)
Q3 = employee_df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = employee_df[
    (employee_df['Salary'] < lower_limit) |
    (employee_df['Salary'] > upper_limit)
]

print(outliers)

# 45. Create and query a MultiIndex by Department and Location.
multi_index_df = employee_df.set_index(
    ['Department', 'Location']
)

print(multi_index_df.head())


# 46. Analyze employee joining counts by year and quarter.
employee_df['JoinYear'] = employee_df['JoiningDate'].dt.year
employee_df['Quarter'] = employee_df['JoiningDate'].dt.quarter

print(employee_df.groupby(['JoinYear', 'Quarter']).size()
)


# 47. Calculate cumulative Salary by department after sorting by Salary.
employees_df = employee_df.sort_values(
    by=['Department', 'Salary']
)

employee_df['CumulativeSalary'] = (
    employee_df.groupby('Department')['Salary']
    .cumsum()
)

print(
    employee_df[
        ['Department',
         'Salary',
         'CumulativeSalary']
    ]
)