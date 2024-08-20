import random

multiplayer = input(
    "Lets play a game of rock paper scissors!\n\nDo you have a friend to play with? Y or N? "
)
multiplayer = multiplayer.lower()
options = ["rock", "paper", "scissors"]

if multiplayer == "n":
    p2_guess = random.choice(options)
    print("Ok you can play against the computer")

play_again = "y"

while play_again == "y":
    print(f"Pick your choice\n{options}")
    p1_guess = input().lower()

    if p1_guess in options:
        print("Ok now player 2's turn")
        p2_guess = input().lower()
        if p2_guess in options:
            # rock beats scissors
            # paper beats rock
            # same guess is a draw
            if p1_guess == p2_guess:
                print("Its a draw! You both entered " + p1_guess)
            elif (
                (p1_guess == "rock" and p2_guess == "scissors")
                or (p1_guess == "paper" and p2_guess == "rock")
                or (p1_guess == "scissors" and p2_guess == "paper")
            ):
                print(p1_guess + " beats " + p2_guess + "! Player 1 wins!")
            else:
                print(p2_guess + " beats " + p1_guess + "! Player 2 wins!")
        else:
            print(p2_guess + " is not a valid option. Try again.")
    else:
        print(p1_guess + " is not a valid option. Try again.")
    play_again = input("Do you want to play again? Y or N ").lower()
