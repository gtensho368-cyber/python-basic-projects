
import random

transmission_rate = 1/20
days_to_recover = 5

def spread(population, infected, can_be_infected, daily_contacts):
    infection_possibility = can_be_infected/population

    total_new_infections = 0
    for member in range(infected):
        contacts = random.randint(0, daily_contacts*2)
        possible_infections = contacts*infection_possibility
        new_victims = possible_infections*transmission_rate
        total_new_infections += new_victims

    return min(round(total_new_infections), can_be_infected)

def heal(infected):
    recovered = 0
    for _ in range(infected):
        rate = random.randint(1, days_to_recover)
        if rate == 1:
            recovered += 1

    return recovered









