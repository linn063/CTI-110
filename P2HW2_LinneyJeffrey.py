#Jeffrey Linney
#3/6/2024
#P2HW2
#Perform statistical computations within a list

grades = []

#Get grades from user

grade1 = float(input("Enter a float"))
grade2 = float(input("Enter a float"))
grade3 = float(input("Enter a float"))
grade4 = float(input("Enter a float"))
grade5 = float(input("Enter a float"))
grade6 = float(input("Enter a float"))

grades.append (grade1)
grades.append (grade2)
grades.append (grade3)
grades.append (grade4)
grades.append (grade5)
grades.append (grade6)
print()
print("------------Results----------------")

#Show lowest grade
grade_min = min (grades)
print (f"Lowest grade:  {grade_min}")

#Show highest grade
grade_max = max (grades)
print (f"Highest Grade: {grade_max}")

#Display sum of gradebook

grade_sum = sum (grades)
print (f"Sum of Grades: {grade_sum}")

#Display average of gradebook and show final output

grade_average = grade_sum / len (grades)
print (f"Average:       {grade_average:.2f}")
print("------------------------------------------")









