#guessing number game
import random
#we use this library to import random num in python
secret_number = random.randint(1, 100)

guess_number=int(input("enter your guess number:"))

if secret_number==guess_number:
    print("correct")
    
else:
    print("guess again")
