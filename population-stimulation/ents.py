
"""Population stimulation for a fictional species(ents)."""
import random

big_ents = 100
small_ents = 100

# mutations 
massive_ents = 0
tiny_ents = 0

baby_big_ents = 0
baby_small_ents = 0

for _ in range(5):
    # big ents have higher chances of being spotted by a preditor
    big_ents -= random.randint(1, 2)
    small_ents -= random.randint(0, 1)
    massive_ents -= random.randint(0, 1) # more aggresive and harder to take down
    tiny_ents -= random.randint(0, 1)

    # reproduction
    baby_big_ents += random.randint(0, 3)

    if baby_big_ents == 3:
        massive_ents += 1

    baby_small_ents += random.randint(0, 3)

    if baby_small_ents == 3:
        tiny_ents += 1

    big_ents += baby_big_ents
    small_ents += baby_small_ents


    print(f"There are {big_ents} big ents.")

    if massive_ents > 0:
        print(f"There are {massive_ents} massive ents.")

    print(f"There are {small_ents} small ents.\n")

    if tiny_ents > 0:
        print(f"There are {tiny_ents} tiny ents.\n")







