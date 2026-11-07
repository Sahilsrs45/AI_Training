hours = int(input("Enter compute hours: "))
storage = int(input("Enter storage used: "))
plan = input("Enter plan (Basic/Premium/Enterprise): ")

if plan == "Basic":
    bill = (hours * 10) + (storage * 2) + 500
elif plan == "Premium":
    bill = (hours * 8) + (storage * 2) + 1000
else: 
    bill = (hours * 10) + (storage * 1) + 2000

print("Total Bill =", bill)