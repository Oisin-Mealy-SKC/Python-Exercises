#A program to demonstrate the single if statement
import random

number = random.randint(1,10)
#pprint (number)

guess = int(input("Enter a number between 1 and 10: "))

#Evaluate the condition
if guess == number:
    print("Good job your guess was right")
    print ("Congratulations")
elif guess != number:
    print ("Wrong, Try again")
   
print ("Goodbye")