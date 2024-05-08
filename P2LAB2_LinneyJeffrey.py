# Jeffrey Linney
# 2/28/2024
# P3LAB2 - Math expressions and f-string

#Get info from user

num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))

# Calculate the product

product = num1 * num2 * num3 * num4

# Calculate average

average = (num1 + num2 + num3 + num4)/4

#Output variables with 0 decimal places

print(f"The product of the numbers is {product: .0f}")
print(f"The average of the numbers is {average: .0f}")
print()

#Output variables with 3 decimal places

print(f"The product of the numbers is {product: .3f}")
print(f"The average of the numbers is {average: .3f}")
