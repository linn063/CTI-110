#Jeffrey Linney
#3/27/2024
#P4LAB2
#Use a While Loop
# Get two integer values from user

var1 = int(input("Enter the smaller integer"))
var2 = int(input("Enter the larger integer"))

#While var1 is larger, allow the user to re-enter the values

while var1 >= var2:
    print("First number must be smaller. Try again")
    var1 = int(input("Enter the smaller integer"))
    var2 = int(input("Enter the larger integer"))

#You were correct and the loop was broken

for num in range(var1, var2+1, 5):
    print(num, end = " ")

    


