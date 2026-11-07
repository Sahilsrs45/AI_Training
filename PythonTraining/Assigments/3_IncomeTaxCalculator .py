income = float(input("Enter annual income: "))
age = int(input("Enter age: "))
investment = float(input("Enter investment amount: "))

if age >= 60:
    income -= 50000

income -= investment

if income < 500000:
    tax = 0
elif income>= 50000 and income <= 1000000:
    tax = income * 0.10
elif income >=1000000 and income <= 2000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax payable:", tax)