from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
spark=(
    SparkSession.builder
    .appName("Employee Analysis")
    .master("local[*]")
    .getOrCreate()
)

# print("Spark application started successfully")
# spark.stop()


employee_data=[
    (101,"Shreyansh","IT",50000,"Noida"),
    (102,"Prince","HR",40000,"Delhi"),
    (103,"Hitesh","Finance",45000,"Gurugram"),
    (104,"Sahil","IT",50000,"Pune"),
    (105,"Pranjali","Sales",50000,"Delhi"),
    (106,"Akash","IT",88000,"Noida"),
    (107,"Shivranjan","HR",55000,"Mumbai"),
    
    
    ]
columns=["employee_id",
         "employee_name",
         "department",
         "salary",
         "city"]

employee_df=spark.createDataFrame(employee_data,
                                  columns)
employee_df.show()
spark.stop()