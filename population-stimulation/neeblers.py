"""Stimulating natural selection with a population of neeblers"""

import random

big_neeblers = 100
small_neeblers = 100

for generation in range(5):
    baby_big_neeblers = 0
    baby_small_neeblers = 0

    # predation
    for _ in range(big_neeblers):
        if random.randint(0, 5) == 5:
            big_neeblers -= 2
            small_neeblers -= 1

    # reproduction
    for _ in range(big_neeblers):
        baby_big_neeblers += random.randint(0, 3)

    for _ in range(small_neeblers):
        baby_small_neeblers += random.randint(0, 3)

    # prevent negative population
    big_neeblers = max(big_neeblers, 0)
    small_neeblers = max(small_neeblers, 0)

    if big_neeblers > 0 or small_neeblers > 0:
        print(f"Generation {generation + 1}:")
        print(f"{big_neeblers} big neeblers.")
        print(f"{small_neeblers} small neeblers.")
        print()
    else:
        print("Extinction!!!")
        break

    # offspring become adults
    big_neeblers = baby_big_neeblers
    small_neeblers = baby_small_neeblers












