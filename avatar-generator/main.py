
import random
import avatar


sizes = ["big", "small"]

for _ in range(3):
    size = random.choice(sizes)
    avatar.bow()
    avatar.eyes(size)
    avatar.nose(size)
    avatar.mouth(size)
    print("\n")


