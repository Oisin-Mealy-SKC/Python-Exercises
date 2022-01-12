import random

Name = input("What is your name: ")

number = random.randint(1, 10)
print (number)

tries = 0

user_guess = int(input("Guess a number 1-10: "))

if number==user_guess:
    print ('Congrats')
    
elif number!=user_guess:
    print ('Hard Luck')
    tries += 1
    
    



    
    