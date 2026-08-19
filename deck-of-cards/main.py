
import random

def get_suit():
    """Returns the suit of the cars"""
    suit = random.randint(1, 4)

    if suit == 1:
        return "Hearts"
    elif suit == 2: 
        return "Diamonds"
    elif suit == 3:
        return "Spades"
    else:
        return "Clubs"

def get_rank(face_cards):
    """Returns the rank of the cards if it has face cards or not"""
    if face_cards:
        cards = random.randint(1, 13)
    else:
        cards = random.randint(2, 10)

    if cards == 1:
        return "Ace"
    elif cards == 11:
        return "Jack"
    elif cards == 12:
        return "Queen"
    elif cards == 13:
        return "King"

    return str(cards)

def draw_card(face_card):
    return f"{get_rank(face_card)} of {get_suit()}"

def draw_hand(num, face_card):
    hand = ""

    for _ in range(num):
        hand += f"{draw_card(face_card)}\n"

    return hand

print(draw_hand(5, True))
print(draw_hand(5, False))











