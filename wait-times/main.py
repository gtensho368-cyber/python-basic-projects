
import random

cashires, cooks  = 3*3, 5 # cashires can take up to three orders
waiting_for_food, waiting_to_order = 0, 0

for serving in range(40*5):
    waiting_to_order += random.randint(0,6)
    orders = min(cashires, waiting_to_order)
    waiting_for_food += min(cashires, orders)
    
    print(f"{waiting_to_order} customers are waiting to order.")
    print(f"{waiting_for_food} customers are waiting for food")

    served = min(cooks, waiting_for_food)
    customers_served = served + serving

print(customers_served)








