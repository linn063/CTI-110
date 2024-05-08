#Jeffrey Linney
#3/27/2024
#P4HW1
#Use a While Loop
# Get integer values from user

num_scores = int(input("How many scores do you want to enter: "))

grades_list = []
for grade in range(num_scores):
    var2 = int(input(f"Enter a score number {grade+1}: "))
    while var2 <0 or var2 >100:
        print("INVALID SCORE ENTERED!!!! Score should be between 0 and 100")
        var2 = int(input(f"Enter a score number {grade+1}:"))

    #You were correct and the loop was broken
    grades_list.append(var2)

#Display Lowest Grade
min_grade = min(grades_list)
grades_list.remove(min_grade)
print (f"Lowest Score: {min_grade}")
print("-------------------Results---------------------")
grade_sum = sum (grades_list)
print(f"Modified List: {grades_list}")

#Display average of gradebook and show final output

grade_average = grade_sum / len (grades_list)
print (f"Scores Average: {grade_average}")

#Determine letter grade for average
print("----------------------------------------------")

if grade_average >= 90:
    print('Grade: A')
   
elif grade_average >= 80:
     print('Grade: B')

elif grade_average >= 70:
    print('Grade: C')

elif grade_average >= 60:
    print('Grade: D')






    


