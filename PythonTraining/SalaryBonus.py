salary=int(input("Enter salary : "))

if salary <30000 :
    salary+=salary*0.05
    
elif salary > 30000 & salary < 50000 :
    salary+=salary*0.1
    
    
else :
    salary+=salary*0.2        
print(salary)
    