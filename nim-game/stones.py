
import random

def computer_pick(stones):
    """Returns the pick of the computer."""
    # returns based on lossing rate
    if stones == 5 or stones <= 2:
        return 1
    elif stones == 3 or stones == 6:
        return 2

    return random.randint(1, 2)

def user_pick():
    """Validates the user pick"""
    removed = 0
    while removed != 1 and removed != 2:
        removed = int(input("How many do you pick up? (1-2) "))
    return removed


def show_game(num_stones):
    """Prints out the stones"""
    display = "o" * num_stones
    return f"{display} ({num_stones} stones)"

def initialize():
    """The starting point of stones."""
    return random.randint(10, 16)


















