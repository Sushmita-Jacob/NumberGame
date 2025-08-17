#Creates random number
import random
number = random.randint(1,100)

#Introduction
print("> This is the Number Guessing Game! I am thinking of a number from 1 to 100, and you must guess it. Are you ready?")
startGame = input("> Type 'yes' or 'no'\n")

#Playing game
while startGame.lower() != "no":
    while startGame.lower() == "yes": #Starts or replays game
        validGuesses = str(list(range(1, 100))) #List of valid guesses (integers between 1 and 100)
        guess = input("\n> Type an integer between 1 to 100 and press enter.\n")

        if guess in validGuesses:
            if int(guess) > number:
                print("> Your guess is too high. Try going lower!")

            elif int(guess) < number:
                print("> Your guess is too low. Try going higher!")
                
            elif int(guess) == number: #User guesses the correct number
                print("> Congratulations! You guessed the number.")
                startGame = input("> Want to play again? Type 'yes' or 'no'.\n").lower()
                number = random.randint(1,100) #Creates new random number

        else: #Redirects user if guess is invalid
            print("> Sorry, your guess must be an integer between 1 and 100. Try again.")

    while startGame.lower() != "yes" and startGame.lower() != "no": #Redirects user if response is invalid
        startGame = input("> Sorry, your response is not valid. Please type yes or no.\n")

#Ends game
while startGame.lower() == "no":
    print("> Maybe some other time then!")
    break