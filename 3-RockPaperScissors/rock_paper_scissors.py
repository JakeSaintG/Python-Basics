import random
from typing import List
import time

possible_moves: List[str] = ["rock", "paper", "scissors"]
goofs = 0
wins = 0
losses = 0
draws = 0
cont = True

while cont:

    print("Rock..")
    time.sleep(0.6)
    print("Paper..")
    time.sleep(0.6)
    print("Scissors..")
    time.sleep(0.6)
    print("Shoot!")
    time.sleep(0.6)
    bot_move: str = possible_moves[random.randint(0, 2)]
    print("RPS-Bot reaches its hand out and starts to form its \"move\". It knows what it is going to play.")

    user_move: str = input("What is your move? \n").lower()
    # TODO: pull out

    print("Your hand shows " + user_move.upper() + " and the bot's hand shows " + bot_move.upper() + "!")
    time.sleep(0.6)
    if user_move == bot_move:
        print("Draw!")
        draws += 1
    elif user_move == "rock":
        if bot_move == "scissors":
            print("You win!")
            wins += 1
        elif bot_move == "paper":
            print("You lose! GOOD DAY!")
            losses += 1
    elif user_move == "paper":
        if bot_move == "rock":
            print("You win!")
            wins += 1
        elif bot_move == "scissors":
            print("You lose! GOOD DAY!")
            losses += 1
    elif user_move == "scissors":
        if bot_move == "paper":
            print("You win!")
            wins += 1
        elif bot_move == "rock":
            print("You lose! GOOD DAY!")
            losses += 1
    else:
        goofs += 1
        if goofs >= 3:
            print("RPS-Bot appears unphased. Your loss counter has incremented by 1.\nIf RPS-Bot could feel, you'd guess that it has grown irritated.")
        else:
            print("RPS-Bot's metal face cocks to side. \nWhile it remains expressionless, you can tell that it is perplexed by the result.")

    i = input("Would you like to continue? yes or no\n")
    if not "y" in i:
        cont = False

print("The game is over.\nYou won " + str(wins) + " time(s).\nRPS-Bot won " + str(losses) + " time(s) with " + str(draws) + " draws.")

if losses > wins:
    print("Overall, you lost.\nRPS-Bot can't look smug.\nStop projecting.")
elif losses == wins:
    print("It looks like a draw overall.")
else:
    print("YOU WON! RPS-Bot sits before you emotionless. In a Terminator-like future, you can bet it will remember this.")