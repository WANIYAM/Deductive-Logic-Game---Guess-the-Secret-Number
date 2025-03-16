'''Write a Python program that implements a deductive logic game where the player must guess a secret three-digit number based on hints.

Game Rules:
The program generate a random three-digit secret number (e.g., "631").
The player has 10 attempts to guess the secret number.
After each guess, the program provides feedback:
“Correct” or 👌 → A correct digit in the correct place.
“Ok” or 👍 → A correct digit in the wrong place.
“Wrong” or ❌ → No correct digits.
The game ends if the player guesses correctly or exhausts all attempts.'''

import random

print("Welcome to the Guessing Game!")
print("You have 10 attempts to guess the secret 3-digit number.\n")

# Generate secret number (digits may repeat)
secret = str(random.randint(100, 999))


# Allow 10 attempts
for attempt in range(1, 11):
    guess = input(f"Attempt {attempt}: Guess a 3-digit number: ")

    # Validate input
    if len(guess) != 3 or not guess.isdigit():
        print("Invalid input! Please enter exactly 3 digits.\n")
        continue  # Skip to the next attempt

    # Check if guess is correct
    if guess == secret:
        print("👌👌👌 You Got IT! Congratulations!\n")
        break

    # Provide feedback
    result = ''
    for i in range(3):
        if guess[i] == secret[i]:
            result += '👌 '  # Correct digit and position
        elif guess[i] in secret:
            result += '👍 '  # Correct digit, wrong position
        else:
            result += '❌ '  # Wrong digit
    print(result + '\n')
else:
    print(f"Game Over! The secret number was: {secret}")
