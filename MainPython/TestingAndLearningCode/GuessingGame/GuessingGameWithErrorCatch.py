import random
import sys, os

tries = 0
num = random.randint(1,10)

while tries < 4:
    try:
        guess = int(input("Enter a number Please"))
        if guess == num:
            print("!"
                  "!!!!!!!!!!!!!YOU WIN!!!!!!!!!!!!!")
            print("\t Do You Want to Play Again")
            break
        elif guess < num:
            print("Guess higher")
        else:
            print("Guess lower")
        tries = tries +1
        print (num)
    except ValueError:
        print('That was not an integer!')
