
import random

bees = random.randint(1000, 6000)
bees_efficiency = random.uniform(0.7, 0.95)
honey = 0

for hours in range(7*18):
    drops = random.randint(50, 300)
    nectar = int((bees*bees_efficiency)-drops)
    deposits = random.randint(500, nectar)

    # Nectar has 75% to 65% water that bees remove
    water_contents = random.uniform(0.25, 0.35)
    honey += round(deposits * water_contents)

print(f"The bees made {honey} grams of honey this week.")





