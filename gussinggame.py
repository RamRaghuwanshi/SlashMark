import random

minimumvalue = 1
maximumvalue = 100
chances = 10


secret_number = random.randint(minimumvalue,maximumvalue)


def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {minimumvalue} and {maximumvalue}: "))
            if minimumvalue <= guess <= maximumvalue:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

def main():
    attempts = 0
    won = False

    while attempts < chances:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    main()