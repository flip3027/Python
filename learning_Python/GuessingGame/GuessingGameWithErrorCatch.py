#! python3
import random
import sys, os

num = random.randint(1,10)
messages =  ["Your guess is to LOW",
             "Your guess is to HIGH",
             "!!!!!!!!!!!!!YOU WIN!!!!!!!!!!!!!",
             "You didn't enter a Integer!"
             ]

print("Guess a number between 1-10:")

for i in range(4):
    try:
        guesses_left = 4 - i
        print("guesses = " + str(guesses_left))

        print("Enter your number:")
        guess = int(input())
        if guess < num:
            print(messages[0])
        elif guess > num:
            print(messages[1])
        else:
            print(messages[2])
            break
    except ValueError:
        print(messages[3])
