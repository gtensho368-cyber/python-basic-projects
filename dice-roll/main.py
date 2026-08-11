
import random

num = int(input("How many times do you want to roll a random number? "))
rolls = 0
limit = 0


for _ in range(num):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sums = dice1 + dice2
    limit += sums

    print(f"You rolled a {sums}.")
    rolls += 1
    average = sums/rolls
    print(average)

    if limit >= 100:
        print(f"You've reached the limit by {limit}.")
        break














