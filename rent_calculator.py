## inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# charge per unit
# Persons living in room/flat

## output
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = " ))
food = int(input("Enter the amount of food orderd = "))
electricity_spend = int(input("Enter the total of electricity spend= "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)


