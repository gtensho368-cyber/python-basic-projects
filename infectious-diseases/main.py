
import virus

population = 1000
infected = 1
contacts = 10
infection_possible = population - infected

for days in range(40):
    if days >= 10:
        contacts = 3

    newly_infected = virus.spread(population, infected, infection_possible, contacts)
    recovered = virus.heal(infected)

    infected += newly_infected - recovered
    infection_possible -= newly_infected

    print(f"{infected} has been infected.")



print("------")
print(f"{population-infection_possible} chickens caught the virus.")











