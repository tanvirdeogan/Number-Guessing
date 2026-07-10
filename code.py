import random
number = random.randint(1, 100)
attempts = 10

print("======NUMBER GUESSING GAME ======")
print("Guess a number between 1 and 100.")
print("You have 10 attempts.")

while attempts > 0:
    guess = int(input("Enter your number: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > number:
        attempts = attempts - 1
        print("Too High")

    else:
        attempts = attempts - 1
        print("Too Low")

    print("Attempts Left:", attempts)
    print()

if attempts == 0:
    print("Game Over!")
    print("The correct number was:", number)