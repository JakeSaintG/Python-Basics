from rps_services import *
import time

goofs = 0
wins = 0
losses = 0
draws = 0
cont = True

print("=========================================================================")
print("The Rock, Paper, Scissors Bot (RPS-Bot) bows as if it were greeting you.")
print("Its metal face is expressionless. It reachs out a balled up fist; ready to\nplay a few games of Rock, Paper, Scissors.")
print("Intructions:")
print("    - Type in Rock, Paper, or Scissors to make a move against the bot.")
print("    - \"r\", \"p\", or \"s\" will also suffice as inputs.")
print("    - RPS-Bot will prompt you at the end of each round to see if you would")
print("    like to continue.")
print("=========================================================================\n")

while cont:

    bot_move = generate_bot_move()

    user_move: str = input("What is your move? \n").lower()

    print("Your hand shows " + user_move.upper() + " and the bot's hand shows " + bot_move.upper() + "!")
    time.sleep(0.6)
    if user_move == bot_move:
        print("Draw!")
        draws += 1
    elif user_move == "rock" or user_move == "r":
        if bot_move == "scissors":
            print("You win!")
            wins += 1
        elif bot_move == "paper":
            print("You lose! GOOD DAY!")
            losses += 1
    elif user_move == "paper" or user_move == "p":
        if bot_move == "rock":
            print("You win!")
            wins += 1
        elif bot_move == "scissors":
            print("You lose! GOOD DAY!")
            losses += 1
    elif user_move == "scissors" or user_move == "s":
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

declare_victory(wins, losses, draws)