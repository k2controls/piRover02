''' Number guessing game to demonstrate Python IDE
'''

#import random
from random import randint

#random_number = random.randint(1, 11)
random_number = randint(1,10)

print(random_number)

username = input("Hello, what's your name? ")

#print("Hello,", username, " Would you like to play a game?")
question = ""
while question != "yes" and question !=  "no":
    question = input("Hello, " + username + "! Would you like to play a game? ")

if question == "no":
    print("Okay? :-(")
    
else:
    #play game
    print("I'm thinking of a number between 1 and 10.")
    play_on = True
    guess_counter = 3
    while play_on:
        guess = input("Have a guess? ")
        guess_num = int(guess)
        if guess_num == random_number:
            print("You won!")
            play_on = False
        elif guess_num < random_number:
            print("You're too low.")
            guess_counter -= 1
        else:
            print("You're too high.")
            guess_counter = guess_counter - 1
        if guess_counter == 0:
            print("You are a loser!")
            break
        else:
            print(guess_counter)


