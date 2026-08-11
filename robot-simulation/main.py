import random
import robot

size = 10
pos = random.randint(1, size)
direction = "right"

print(robot.platform(pos, size, direction))

for _ in range(3):
    action = random.randint(1, 2)
    if action == 1:
        pos = robot.move_bot(pos, size, direction)
    else:
        direction = robot.reverse(direction)
        
    print(robot.platform(pos, size, direction))







