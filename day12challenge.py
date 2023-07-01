#guess-the-number
from art_and_data import day12challenge_art
print(day12challenge_art.logo)
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
Choose=input("Choose a difficulty. Type 'easy' or 'hard':")

random_num=random.randint(1,100)
print(random_num)


def check(max):
    print(f"You have {max} attempts remaining to guess the number.")
    number=int(input("Make a guess:"))
    for i in range(1,max):
        if number<random_num:
            print("Too low.")
            print("Guess again.")
            print(f"You have {max-i} attempts remaining to guess the number.")
            number=int(input("Make a guess:"))
        elif number>random_num:
            print("Too high.")
            print("Guess again.")
            print(f"You have {max-i} attempts remaining to guess the number.")
            number=int(input("Make a guess:"))
        elif number==random_num:
            print(f"You got it! The answer was {random_num}.")
            break
    print("You've run out of guesses, you lose.")

if Choose=="easy":
    max1=5
    check(max1)
elif Choose=="hard":
    max2=3
    check(max2)








