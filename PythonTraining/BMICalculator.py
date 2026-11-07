weight=float(input("Enter weight :"))
height=float(input("Enter height :"))

BMI=weight/(height**2)

if BMI <18.5 :
    print("underweigh")
    
elif BMI >18.5 & BMI<24.9 :
    print("normal")    
    
elif BMI>25 & BMI<29.9 :
    print("overweight")    
    
else :
    print("Obese")    