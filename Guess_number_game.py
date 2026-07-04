import random

print("=" * 40)
print("      GUESS THE NUMBER GAME")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0

print("I have chosen a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations!")
        print(f"You guessed the number {secret_number} correctly.")
        print(f"It took you {attempts} attempts.")
        break

print("=" * 40)
print("      Thanks for Playing!")
print("=" * 40)
