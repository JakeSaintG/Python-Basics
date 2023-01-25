import random
import time
from typing import List

possible_moves: List[str] = ["rock", "paper", "scissors"]

def declare_victory(w, l, d):
        
    print("\nThe game is over.\nYou won " + str(w) + " time(s).\nRPS-Bot won " + str(l) + " time(s) with " + str(d) + " draws.")

    if l > w:
        print("\nOverall, you lost.\nRPS-Bot can't look smug.\nStop projecting.")
    elif l == w:
        print("\nIt looks like a draw overall.")
    else:
        print("\nYOU WON! RPS-Bot sits before you emotionless. In a Terminator-like future, you can bet it will remember this.")


def generate_bot_move():
    print("Rock..")
    time.sleep(0.6)
    print("Paper..")
    time.sleep(0.6)
    print("Scissors..")
    time.sleep(0.6)
    print("Shoot!")
    time.sleep(0.6)
    print("RPS-Bot reaches its hand out and starts to form its \"move\". It knows what it is going to play.")
    #random.choice(["rock", "paper", "scissors"]) would also have worked
    return possible_moves[random.randint(0, 2)]