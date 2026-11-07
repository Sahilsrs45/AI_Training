salary=float(input("Enter salary"))
credit_score=float(input("enter credit score"))
loan_amount=float(input("enter existing loan amount"))
employment_type=input("enter employment type")

if salary>80000 and credit_score>750 and loan_amount<20000:
    print("loan approved immediately")
elif salary>50000 and credit_score>650:
    print("approved with caution")
    
elif credit_score<600:
    print("rejected")
    
else :
    print("under manual review")        