import random

Name =("What is your name:")
print (Name)

number= random.randint(1,10)
#print (number)

guess = int(input("Enter a number between 1 and 10: "))

if guess == number:
    print ("Your guess was correct")
    print ("Well Done")
    
elif guess < number:
    print ("Hard Luck")
    print ("Too Low")
else:
    print ("Hard Luck")
    print ("Too High")
    
if guess > 10 :
    print ("Please choose number between 1 and 10")


print ("Goodbye",Name)
    