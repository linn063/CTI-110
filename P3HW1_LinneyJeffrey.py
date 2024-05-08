#Jeffrey Linney
#March 18/2024
#P3HW1
# Linney


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
# add grades entered to a list
grades = []

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades.append (mod_1)
grades.append (mod_2)
grades.append (mod_3)
grades.append (mod_4)
grades.append (mod_5)
grades.append (mod_6)

print()
print("--------------Results----------------")


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# Determine lowest, highest , sum and average for grades

grade_low = min(grades)
print(f"Lowest Grade: {grade_low}")

grade_high = max(grades)
print(f"Highest Grade: {grade_high}")

grade_total = sum(grades)
print(f"sum of grades: {grade_total}")

grade_average = grade_total / len(grades)
print(f"average: {grade_average:.2f}")


# determine letter grade for average


if grade_average >= 90:
    print('Your grade is: A')

        
elif grade_average >= 80:
     print('Your grade is: B')

elif grade_average >= 70:
    print('Your grade is: C')

elif grade_average >= 60:
    print('Your grade is: D')
else:
    print('You need to perform better')







