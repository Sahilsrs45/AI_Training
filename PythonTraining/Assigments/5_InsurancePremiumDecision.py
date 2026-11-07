age = int(input("Enter age: "))
smoker = input("Are you a smoker? : ")
bmi = float(input("Enter BMI: "))
disease = input("Pre-existing disease : ")

if disease == "yes" and age > 60:
    print("Insurance Rejected")
elif smoker == "yes" and age > 50:
    print("High Premium")
elif bmi > 25:
    print("Medium Premium")
else:
    print("Low Premium")
