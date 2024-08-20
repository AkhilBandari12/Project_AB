from random import randint

print(
    "Lets play a guessing game. I'll think of a number between 1 and 10 and you have to guess it."
)

answer = randint(1, 11)

guess = int(input("Ok! Lets play. What number am i thinking of?"))

while guess != answer:
    if guess > answer:
        lower_or_higher = "lower"
    else:
        lower_or_higher = "higher"

    print(f"Wrong! Guess {lower_or_higher}...")
    guess = int(input())

print("Well done, you guessed it!")
