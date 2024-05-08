#Jeffrey Linney
#April 24, 2024
#P5HW Homework
#Loops & Functions - Math Quiz
import random
#Creating a Quiz of Simple Addition and Subtraction

def add_random_number():
       

    #Create random nums
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    result = rand_num1 + rand_num2
    print(f"{rand_num1} + {rand_num2}")
    total_guesses = 1
    guessed_answer = int(input("Please give an answer: "))
    while guessed_answer != result:
        total_guesses += 1
        if guessed_answer > result:
            print ("Your Answer is Too High")

        if guessed_answer < result:
            print("Your Answer is Too Low")
        guessed_answer = int(input("Please Try Again"))
                             
        
    print("Your Answer is Correct!")
            
    print(f"It took you {total_guesses} guesses")
    
def subtract_random_number():
       

    #Create random nums
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    result = rand_num1 - rand_num2
    print(f"{rand_num1} - {rand_num2}")
    total_guesses = 1
    guessed_answer = int(input("Please give an answer: "))
    while guessed_answer != result:
        total_guesses += 1
        if guessed_answer > result:
            print ("Your Answer is Too High")

        if guessed_answer < result:
            print("Your Answer is Too Low")
        guessed_answer = int(input("Please Try Again"))
                             
        
    print("Your Answer is Correct!")

    print(f"It took you {total_guesses} guesses")


def main():
    print("Welcome to Math Quiz")
    print()
    print()
    print("MAIN MENU")
    print("------------")
   
    num = int(input("Please choose one of the menu options: "))
    while num != 3:
        if num == 1:
            print("1. Adding Random Numbers")
            add_random_number()
                
        if num == 2:
            print ("2. Subtracting Random Numbers")
            subtract_random_number()
        num = int(input("Please choose one of the menu options: "))

    #Loop is Broken
    print("3. Exit")
    


main()
    


    
