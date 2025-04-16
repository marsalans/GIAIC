import random

def guess_the_number():
    random_number = random.randint(1, 100)
    guess_left = 5
    print("Guess the number (between 1 and 100): ")

    while guess_left > 0:
        print(f"\n{guess_left} guess(es) remaining")
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Incorrect input. Please enter a valid number.")
            continue

        if guess < random_number:
            print("Input a higher number.")
        elif guess > random_number:
            print("Input a lower number.")
        else:
            print("You've guessed the number right!")
            return

        guess_left -= 1

    print(f"\n You've reached the limit. The correct number was {random_number}.")

guess_the_number()
