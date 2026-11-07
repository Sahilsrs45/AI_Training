employee_rating =int(input("Enter rating : "))

years_of_experience=float(input("Enter year of experience")) 

project_delivery_status=input("enter deleivery status : ")

if employee_rating==5 and years_of_experience>10 and project_delivery_status=="on time":
    print("30% bonus")
elif employee_rating==4 and years_of_experience > 7 :
    print("20% bonus")
elif employee_rating==3 and project_delivery_status=="delayed":
    print("5% bonus")  
else :
    print("no bonus")          
