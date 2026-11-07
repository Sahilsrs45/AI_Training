import numpy as np

salary=np.array([65000,58000,72000,80000,85000,68000,90000,76000])
print("===============Salary==============")

print(salary)

print("salary operations-: ")
print("Array: ",salary)
print("Type : ",type(salary))
print("Dimensions: ",salary.ndim)
print("Shape: ",salary.shape)
print("Size :",salary.size)
print("Data type: ", salary.dtype)
# salary=np.array([[[65000,58000,72000,80000,85000,68000,90000,76000]]])
# print(salary.shape)
# print(salary.ndim)

rating=np.array([4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3])

print("===========Rating operations==========")

print(rating)
print("Type: ",type(rating))
print("Dimensions: ",rating.ndim)
print("Shape: ",rating.shape)
print("Rating size ",rating.size)
print("Data type: ",rating.dtype)

#numpy indexing
print("==========Numpy Indexing========")
print("First salary:",salary[0])
print("Third salary : ",salary[2])
print("Last Salary :",salary[-1])
print("Second last salary: ",salary[-2])
print("Third last salary : ",salary[-3])

print("==========Numpy slicing========")
print(salary[0:3])

#last 3
print(salary[-3:])

#all except 1st 2
print(salary[2:])

print("=============Salary above 75000")
high_salary=salary[salary>75000]
print("Employee salary : ",high_salary)
print("Employee count ",len(high_salary))

print("========rating ======")
high_rating=rating[rating>4.5]

print("Rating ",high_rating)
print("No of employees ",len(high_rating))

#conditional salary 
new_salary=np.where(salary < 70000 ,salary*1.10,salary*1.05)
print("Original salary:",salary)
print("updated salary",new_salary)


#performance bonus
print("Performance bonus")
bonus=np.where(
    rating>=4.5,
    salary*0.15,
    salary*0.05
)
print(bonus)

#salary after bonus
salary_with_bonus=salary+bonus
print("Original salary",salary)
print("Bonus",bonus)
print("salary after bonus",salary_with_bonus)

