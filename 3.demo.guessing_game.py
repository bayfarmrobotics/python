import random
rng = random.Random()

number = rng.randrange(1,100000000)
guesses = 0
message = ""

while True:
    guess = int(input(message + "\nGuess my number between 1 and 1000: "))
    guesses += 1 
    if guess > number:
        message += str(guess) + "is too high.\n"
    elif guess <number:
        message += str(guess) + " is too low.\n"
    else:
        break
input("\n\nGreat, you got it in "+str(guesses)+" guesses!\n\n")