
import random #creating secret_number

print "Hello, welcome to the number guessing game!" #welcoming player
raw_input("What is your name? ") # asking for name

secret_number = random.randint(1, 100) #secret number parameters
guess = None #to be filled with raw input from player
too_low = 0
too_high = 101
try: #initiate assessment: is this an integer?

    guess = int(input("Guess a number between 1 and 100 ")) #accepts input and turns into an integ

    while secret_number != guess: #while the random number does not equal the guess...
        if guess < 1 or guess > 100:
            print "You sack of wine! Stay within the parameters!"
            guess = int(input("Guess a number between 1 and 100 "))
        elif guess > secret_number: #if the guess is higher, guess again
            print "Your guess is too high"
            guess = int(input("Guess a number between 1 and 100 "))
        elif guess < secret_number: #if the guess is lower, guess again
            print "Your guess is too low"
            guess = int(input("Guess a number between 1 and 100 "))

except NameError:
    print("Do you even know what an integer is?!")

redo = raw_input("Good Job! Would you like to play again? (Y or N)")
    if redo == "Y":
        #play again
    else:
        "You suck!"

 