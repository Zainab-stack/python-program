import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))

if guess == number:
    print("You won!")
else:
    print("Try again!")
