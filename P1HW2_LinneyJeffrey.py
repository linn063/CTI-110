# Jeffrey Linney
# Februray 19, 2024
# P1HW2
## This program calculates and displays travel expenses

'''
Get a travel budget from user
Get an intended destination from user
Get estimated travel expenses from user (gas, hotel, food)
Total all expenses
Subtract total expenses from travel budget
Display ending budget
'''

# Get input from user

# Enter your Budget
Budget = int(input("Enter your budget: "))
print (Budget)

# Enter your Destination
Destination = str(input("Enter your travel destination: "))
print (Destination)

# Enter your gas expense
Gas = int(input("Enter the amount you will spend on gas: "))
print (Gas)

# Enter your hotel expense
Accomodation = int(input("Enter the amount you will spend on hotel: "))
print (Accomodation)

# Enter your food expense
Food = int(input("Enter the amount you expect to pay on food: "))

print (Food)

total = Budget


Expenses = Gas + Accomodation + Food
print (Expenses)

Remaining_Balance = Budget - Expenses

print (Budget, "-", Gas, "+", Accomodation, "+", Food, "=" ,Remaining_Balance)

print ("----------Travel Expense----------")
print ("Location", Destination)
print ("Initial Budget", Budget)
print()
print()

print ("Fuel", Gas)
print ("Accomodation", Accomodation)
print ("Food", Food)
print()
print()

print ("Remaining Balance", "=", Remaining_Balance)

                        
