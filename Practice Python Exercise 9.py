# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def guess_the_number():
    print("Welcome to the game, Guess The Number!"\
    "\nA random number will be picked from 1-9." \
    "\nYou will have to guess it. " \
    "\nIf your guess is wrong, you will be told if you guessed too low or too high." \
    "\nThe game stops if you guess the correct number or if you type exit.")

    random_number = random.randint(1,9)
    game_count = 0
    continue_game = True

    while continue_game:
        try:
            guess = input("Type your guess or type 'exit' to stop the game: ")
            if guess.lower().strip()=="exit":
                print(f"Game ends. You took {game_count}","try" if game_count==1 else "tries")
                break

            game_count += 1
            if int(guess)==random_number:
                print(f"You guessed correctly in {game_count}", "try!" if game_count==1 else "tries!",f"The random number is {random_number}")
                continue_game = False
            else:
                print("Too", "low!" if int(guess) <= random_number else "high!",  "Try again")
        except ValueError:
            print("Incorrect response. Try again")
            continue

if __name__ == "__main__":
    guess_the_number()






                

