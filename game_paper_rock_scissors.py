import random

choices = ["rock","paper","scissors"]
comp_win = 0
play_win = 0

while True:
    computer = random.choice(choices)
    player = ""
    
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        result = "Tie!"

    elif player == "rock":
        if computer == "paper":
            result = "You lose!"
            comp_win += 1
        if computer == "scissors":
            result = "You win!"
            play_win += 1

    elif player == "scissors":
        if computer == "rock":
            result = "You lose!"
            comp_win += 1
        if computer == "paper":
            result = "You win!"
            play_win += 1

    elif player == "paper":
        if computer == "scissors":
            result = "You lose!"
            comp_win += 1
        if computer == "rock":
            result = "You win!"
            play_win += 1

    print("computer: ",computer)
    print("player: ",player)
    print(result)

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print(f'Bye! you won {play_win} times and the computer {comp_win}')