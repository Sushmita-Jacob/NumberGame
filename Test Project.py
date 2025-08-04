#Creates random number
import random
number = random.randint(1,100)

#Introduction
print("This is the Number Guessing Game! I am thinking of a number from 1 to 100, and you must guess it. Are you ready?")
startGame = input("Type 'yes' or 'no'\n")

#Playing game
while startGame.lower() == "yes":
    print("\nWARNING: Typing a letter or decimal will result in an error.")
    guess = input("Type an integer between 1 to 100 and press enter.\n")

    if int(guess) <= 100 and int(guess) >= 0:
        if int(guess) > number:
             print("Your guess is too high. Try going lower!")

        elif int(guess) < number:
            print("Your guess is too low. Try going higher!")
       
        elif int(guess) == number:
            print("Congratulations! You guessed the number.")
            break

    else:
        print("Sorry, your guess must be an integer between 1 and 100. Try again.")

if startGame.lower() == "no":
    print("Maybe some other time then!")