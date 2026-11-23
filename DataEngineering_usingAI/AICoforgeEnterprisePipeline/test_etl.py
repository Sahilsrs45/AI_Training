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


def employee_analysis(df):
    # Q1. Read all five departmental CSV files into separate Pandas DataFrames.

  it_df = pd.read_csv("data/employees/it_employees.csv")
  print(it_df.head(5))
  hr_df = pd.read_csv("data/employees/hr_employees.csv")
  print(hr_df.head(5))
  finance_df = pd.read_csv("data/employees/finance_employees.csv")
  print(finance_df.head(5))
  sales_df = pd.read_csv("data/employees/sales_employees.csv")
  print(sales_df.head(5))
  operations_df = pd.read_csv("data/employees/operations_employees.csv")
  print(operations_df.head(5))
  
  
  #Q2. Combine all five DataFrames into one employee_df using pd.concat(). 
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  employee_df=pd.concat([it_df,hr_df,finance_df,sales_df,operations_df])
  print(employee_df.head)

  #Q3. Display the first 20 employee records from the consolidated DataFrame. 
  print("Top 20 employees :",employee_df.head(20))
  
  
  #Q4. Display the last 20 employee records. 
  print("Last 20 employees :",employee_df.tail(20))
   
   
  #Q5. Find the total number of employees across all departments. 
  print(len(employee_df))

  #Q6. Display the column names and data types of employee_df. 
  print(employee_df.columns)
  print(employee_df.dtypes)

  #Q7. Check whether any column contains missing values. 
  print(employee_df.isnull().sum())

  #Q8. Identify duplicate records based on emp_id. 
  duplicate_records=employee_df[employee_df.duplicated(subset="emp_id")]
  print("Duplicate reccords :",duplicate_records)

  #Q9. Display the number of employees in each department. 
  employee_count=employee_df["department"].value_counts()
  print("Count by department :",employee_count)

  #Q10. Find the total number of unique cities in the dataset. 
  print("Unique cities: ",employee_df["city"].nunique())
  
  
  #Section 2: Basic Filtering and Selection  |  Questions 11–20 

  #Q11. Display all employees working in the IT department. 
  print("Employee with Department IT ",employee_df[employee_df["department"]=="IT"])

  #Q12. Find employees working in the Finance department. 
  print("Employee with Department Finance ",employee_df[employee_df["department"]=="Finance"])
  

  #Q13. Display employees whose salary is greater than ₹100,000.
  print("Employee with salary > 100000 ",employee_df[employee_df["salary"]>100000]) 

  #Q14. Find employees earning between ₹50,000 and ₹90,000. 
  print("Employee with salary between 50k and 90k ",employee_df[(employee_df["salary"]>=50000) & (employee_df["salary"]<=90000)])

  #Q15. Display all employees located in Pune. 
  print("Employee with city Pune:  ",employee_df[employee_df["city"]=="Pune"])

  #Q16. Find employees working in IT and located in Bangalore. 
  print("Employee with Department IT and city is Banglore ",employee_df[(employee_df["department"]=="IT") & (employee_df["city"]=="Banglore")])

  #Q17. Display Finance employees earning more than ₹80,000. 
  print("Employee with Department Finance ang earning more than 80k ",employee_df[(employee_df["department"]=="Finance") & (employee_df["salary"]>80000)])

  #Q18. Find employees belonging to either HR or Sales. 
  print("Employee with Department is HR or Sales ",employee_df[(employee_df["department"]=="HR") | (employee_df["department"]=="Sales")]) 

  #Q19. Display employees whose salary is less than ₹40,000 and who work in Chennai. 
  print("Employee with salary > 40k and location is Chennai: ",employee_df[(employee_df["salary"]<40000) & (employee_df["city"]=="Chennai")]) 
  

  #Q20. Find all employees whose city is not Mumbai.
  print("Employee with city is not Mumbai:  ",employee_df[employee_df["city"]!="Mumbai"])
  
  #Section 3: SUM and Total Salary Calculations  |  Questions 21–30 

  #Q21. Calculate the total salary expenditure across all five departments. 
  print("Total salary sum",employee_df["salary"].sum())

  #Q22. Calculate the total salary paid to IT employees.
  print("Total salary sum of IT",employee_df[employee_df["department"]=="IT"]["salary"].sum())
   

  #Q23. Calculate the total salary paid to HR employees. 
  print("Total salary sum for HR department",employee_df[employee_df["department"]=="HR"]["salary"].sum())

  #Q24. Calculate the total salary paid to Finance employees. 
  print("Total salary sum for Finance",employee_df[employee_df["department"]=="Finance"]["salary"].sum())


  #Q25. Calculate the total salary paid to Sales employees. 
  print("Total salary sum for Sales",employee_df[employee_df["department"]=="Sales"]["salary"].sum())

  #Q26. Calculate the total salary paid to Operations employees. 
  print("Total salary sum for Operations department",employee_df[employee_df["department"]=="Operations"]["salary"].sum())

  #Q27. Calculate department-wise total salary expenditure using groupby(). 
  salary_expenditure=employee_df.groupby("department")["salary"].sum()
  print(salary_expenditure)

  #Q28. Calculate city-wise total salary expenditure. 
  city_salary_expenditure=employee_df.groupby("city")["salary"].sum()
  print(city_salary_expenditure)

  #Q29. Find the combined salary expenditure for IT and Finance. 
  combined_salary=employee_df[(employee_df["department"]=="IT") | (employee_df["department"]=="Finance")]["salary"].sum()
  print("Combined salary :",combined_salary)

  #Q30. Calculate each department's percentage contribution to the company's total salary expenditure.
  total_sal=employee_df["salary"].sum()
  dept_percentageContribution=((employee_df.groupby("department")["salary"].sum())/total_sal)*100
  print("Department wise percentage : ",dept_percentageContribution)


  #Q31. Find the maximum salary across the company. 
  print("max salary :",employee_df["salary"].max())

  #Q32. Find the minimum salary across the company. 
  print("min salary :",employee_df["salary"].min())

  #Q33. Calculate the average salary of all employees. 
  print("Average salary :",employee_df["salary"].mean())

  #Q34. Find the maximum salary in each department. 
  print("Max salary dept wise : ",employee_df.groupby("department")["salary"].max())

  #Q35. Find the minimum salary in each department. 
  print("Min salary dept wise : ",employee_df.groupby("department")["salary"].min())

  #Q36. Calculate the average salary in each department.
  print("Average salary dept wise : ",employee_df.groupby("department")["salary"].mean()) 

  #Q37. Find the maximum salary in each city. 
  print("Max salary city wise : ",employee_df.groupby("city")["salary"].max())

  #Q38. Find the minimum salary in each city. 
  print("Min salary city wise : ",employee_df.groupby("city")["salary"].min())

  #Q39. Calculate the average salary for employees in Pune. 
  print("Average salary for Pune employees",employee_df[employee_df["city"]=="Pune"]["salary"].mean())

  #Q40. Find the difference between maximum and minimum salary for every department. 
  
  salary_diff = (
    employee_df.groupby("department")["salary"].max()
    - employee_df.groupby("department")["salary"].min()
)

  print("Difference between max and min salary dep wise:",salary_diff)

  

  #Q41. Group employees by department and calculate employee count. 
  empCountByDept=employee_df.groupby("department")["emp_id"].count()
  print("Emp count by dept:",empCountByDept)

  #Q42. Group employees by city and calculate employee count.
  empCountByCity=employee_df.groupby("department")["emp_id"].count()
  print("Emp count by city:",empCountByDept)
   

  #Q43. Group by department and calculate total salary, average salary, minimum salary and maximum salary in one DataFrame. 
  dept_salary_summary=employee_df.groupby("department")["salary"].agg(["sum","mean","min","max"])
  print(dept_salary_summary)
  #Q44. Group by department and city and calculate total salary.
  print("Total salary be dep and city: ",employee_df.groupby(["department","city"])["salary"].sum()) 

  #Q45. Group by department and city and calculate average salary. 
  print("Avg salary be dep and city: ",employee_df.groupby(["department","city"])["salary"].mean()) 
  

  #Q46. Group by department and city and calculate employee count. 
  print("Total count by dep and city: ",employee_df.groupby(["department","city"])["emp_id"].count()) 

  #Q47. Find the department with the highest total salary expenditure. 
  print("HIghest total salary expenditure:",employee_df.groupby("department")["salary"].sum().idxmax())

  #Q48. Find the department with the lowest average salary. 
  print("Lowest avg salary expenditure:",employee_df.groupby("department")["salary"].mean().idxmin())
  

  #Q49. Find the city with the highest number of employees. 
  print("City with max no of employee :",employee_df.groupby("city")["emp_id"].max().idxmax())

  #Q50. Create a department-wise salary summary sorted by total salary in descending order. 
  dept_summary=employee_df.groupby("department")["salary"].agg(["sum","min","max","mean"]).sort_values(by="sum",ascending=False)
  print(dept_summary)
   

  #Q51. Find departments whose total salary expenditure exceeds ₹10,000,000. 
  dept_totalSalary=employee_df.groupby("department")["salary"].sum() 
  print(dept_totalSalary[dept_totalSalary>10000000])


  #Q52. Find departments whose average salary exceeds ₹90,000. 
  dept_avg_salary = employee_df.groupby("department")["salary"].mean()

  print(
    dept_avg_salary[ dept_avg_salary > 90000])
 
  #Q53. Find departments whose minimum salary is greater than ₹25,000. 
  dept_min_salary=employee_df.groupby("department")["salary"].min()
  print("min salary > 25000")
  print(dept_min_salary[dept_min_salary>25000])

  #Q54. Find departments whose maximum salary exceeds ₹140,000. 
  dept_maxSalary=employee_df.groupby("department")["salary"].max()
  print(dept_maxSalary[dept_maxSalary>140000])

  #Q55. Find cities where the total salary expenditure exceeds ₹15,000,000. 
  city_total_salary=employee_df.groupby("city")["salary"].sum()
  print(city_total_salary[city_total_salary >15000000])

  #Q56. Find department-city combinations whose average salary exceeds ₹100,000. 
  dept_city_avgSalary=employee_df.groupby(["department","city"])["salary"].mean()
  print(dept_city_avgSalary[dept_city_avgSalary > 100000])

  #Q57. Find departments having more than 150 employees. 
  dept_count=employee_df.groupby("department")["emp_id"].count()
  print(dept_count[dept_count > 150])

  #Q58. Find cities having more than 100 employees.
  city_count=employee_df.groupby("city")["emp_id"].count()
  print(city_count[city_count > 100]) 

  #Q59. Find department-city combinations whose total salary exceeds ₹3,000,000.
  dept_city_totalSalary=employee_df.groupby(["department","city"])["salary"].sum()
  print(dept_city_totalSalary[dept_city_totalSalary > 3000000]) 

  #Q60. Find departments whose average salary is greater than the overall company average salary.
  dept_avg_salary=employee_df.groupby("department")["salary"].mean()
  avg_salary=employee_df["salary"].mean()
  print(dept_avg_salary[dept_avg_salary> avg_salary])
  
  
  #Q61. Create a department-wise summary containing total salary, average salary, maximum salary, minimum salary and employee count. 
  dept_wise_summary=employee_df.groupby("department")["salary"].agg(["sum","mean","max","min","count"]) 
  print(dept_wise_summary)
  #Q62. Create a city-wise summary containing total salary, average salary and employee count. 
  city_wise_summary=employee_df.groupby("city")["salary"].agg(["sum","mean","count"])  
  print(city_wise_summary)  
  #Q63. Calculate the salary range (maximum minus minimum) for every department. 
  max_dept_salary=employee_df.groupby("department")["salary"].max()
  min_dept_salary=employee_df.groupby("department")["salary"].min()
  salary_range= max_dept_salary -min_dept_salary
  print("salary range : ",salary_range)
  
  

  #Q64. Calculate the salary standard deviation for each department. 
  print(employee_df.groupby("department")["salary"].std())

  #Q65. Calculate the median salary for each department. 
  print(employee_df.groupby("department")["salary"].median())
  

  #Q66. Calculate the 25th and 75th salary percentiles for each department. 
  print(employee_df.groupby("department")["salary"].quantile([0.25, 0.75]))

  #Q67. Find the top three departments by average salary. 
  top_three_dept=employee_df.groupby("department")["salary"].mean().sort_values(ascending=False).head(3)
  print(top_three_dept) 
  #Q68. Find the top three cities by total salary expenditure. 
  top_three_cities=employee_df.groupby("city")["salary"].sum().sort_values(ascending=False).head(3)
  print(top_three_cities)
  

  #Q69. Find the department-city combination with the highest average salary. 
  dept_city_comb=employee_df.groupby(["department","city"])["salary"].mean().sort_values(ascending=False).head(1)
  print(dept_city_comb) 
  #Q70. Calculate each department's share of total employees and total company salary. 
  
  dept_summary=employee_df.groupby("department").agg(
      employee_count=("emp_id","count"),
      total_salary=("salary","sum")
  )
  
  dept_summary["employee_)share_percent"]=(
      dept_summary["employee_count"]/dept_summary["employee_count"].sum()
  )*100
  
  dept_summary["salary_share_percent"] = (
    dept_summary["total_salary"]
    / dept_summary["total_salary"].sum()
) * 100
  
  print("dept summary :",dept_summary)
  
  
  #Q71. Create a department salary summary DataFrame and merge it with employee_df using department. 
  dept_salary_summary = (
    employee_df.groupby("department", as_index=False)["salary"]
    .sum()
    .rename(columns={"salary": "department_total_salary"})
)

  merged_df = pd.merge(
    employee_df,
    dept_salary_summary,
    on="department",
    how="left"
)

  print(merged_df)
  
  #Q72. Create a city salary summary DataFrame and merge it with employee_df using city. 
  city_salary_summary=employee_df.groupby("city",as_index=False)["salary"].sum()
  city_salary_summary.rename(columns={"salary": "city_total_salary"},inplace=True)
  
  merged_df1=pd.merge(employee_df,city_salary_summary,
                      on="city",
                      how="left")
  print(merged_df1)
  
  #Q73. Create a department employee-count DataFrame and merge it with employee_df. 
  department_employeeCount=employee_df.groupby("department",as_index=False)["emp_id"].count().rename(
      columns={"emp_id":"department_emp_count"}
  )
  merged_df3=pd.merge(employee_df,department_employeeCount,
                      on="department",
                      how="left")
  print(merged_df3)

  #Q74. Create a department average-salary DataFrame and merge it with employee_df. 
  
  dept_averageSalary=employee_df.groupby("department",as_index=False)["salary"].mean().rename(
      columns={"salary":"dept_avg_salary"}
  )
  
  merged_df4=pd.merge(
      employee_df ,dept_averageSalary,
      on="department",
      how="left"
  )
  print(merged_df4)

  #Q75. After merging department averages, find employees earning more than their department's average salary. 
  dept_avg=employee_df.groupby("department",as_index=False)["salary"].mean().rename(
      columns={"salary":"avg_salary"}
  )
  merged_dfSal=pd.merge(employee_df,dept_avg,
                        on="department",
                        how="left")
  
  print(merged_dfSal[merged_dfSal["salary"]> merged_dfSal["avg_salary"]])
  
  #Q76. After merging city averages, find employees earning less than their city's average salary.
  city_salary=employee_df.groupby("city",as_index=False)["salary"].mean().rename(
      columns={"salary":"city_salary"}
  ) 
  
  merged_citySal=pd.merge(employee_df,city_salary,
                          on="city",
                          how="left")
  
  print(merged_citySal[merged_citySal["salary"]>merged_citySal["city_salary"]])

  #Q77. Create separate department salary-total and employee-count summary DataFrames and merge them. 
  dept_salary=employee_df.groupby("department",as_index=False)["salary"].sum().rename(
      columns={"salary":"dept_sal"}
  ) 
  
  employee_count=employee_df.groupby("department",as_index=False)["emp_id"].count().rename(
      columns={"emp_id":"emp_count"}
  )
  
  merged_emp_count=pd.merge(dept_salary,employee_count,
                            on="department",
                            how="inner")
  print(merged_emp_count)
  
  #Q78. Merge department maximum-salary data with employee_df and identify employees earning the department maximum. 

  dept_maxSalary=employee_df.groupby("department",as_index=False)["salary"].max().rename(
      columns={"salary":"maxSalary"}
  ) 
  
  merged_dept=pd.merge(employee_df,dept_maxSalary,
                       on="department",
                       how="left")
  
  print(merged_dept)
  
  #Q79. Create department-city salary and employee-count summaries and merge them using both department and city. 
  dept_city_salary=employee_df.groupby(["department","city"],as_index=False)["salary"].sum().rename(
      columns={"salary":"total_salary"}
  )
  
  dept_employee_count=employee_df.groupby(["department","city"],as_index=False)["emp_id"].count().rename(
      columns={"emp_id":"emp_count"}
  )
  
  merge_dept_city_employee=pd.merge(dept_city_salary,dept_employee_count,
                                    on=["city","department"])
  
  print(merge_dept_city_employee)
  
  
  #Q80. Demonstrate inner, left, right and outer joins using a department summary and a department reference DataFrame constructed from the existing data.
  
  
def run_etl():
   original = extract_employees()
   cleaned, rejected = transform_employees(original)
   employee_analysis(cleaned)
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
   
if __name__ == "__main__":
    result = run_etl()
    print(result)   