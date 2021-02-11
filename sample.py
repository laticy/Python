import random

numberofguesses = int(input("How many guesses would you like? "))
correctguess = random.randint(1,10)
correct = False
guesscount = 0

while guesscount < numberofguesses:
    currentguess = int(input("Enter your guess "))
    if currentguess > correctguess:
        print(f"Your guess was too high. You have: {numberofguesses - guesscount} remaining" )
        guesscount =+ 1
    elif currentguess < correctguess:
        print(f"Your guess was too low. You have: {numberofguesses - guesscount} remaining" )
        guesscount += 1
    else:
        correct = True
        break

if correct:
    print("You guessed correctly! You win!")
else:
    print("Sorry you lose")