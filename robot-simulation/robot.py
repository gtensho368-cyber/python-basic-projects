
def platform(pos, size, direction):
    grid = "|"

    for _ in range(size):
        if _ == pos - 1:
            robot = robot_direction(direction)
            grid = grid + robot
        else:
            grid = grid + " . "

    return grid + "|"

def robot_direction(direction):
    robot = " < " if direction == "left" else " > "
    return robot

def move_bot(pos, size, direction):
    if direction == "left":
        return max(1, pos-1)
    else:
        return min(pos+1, size)

def reverse(direction):
    if direction == "left":
        return "right"
    elif direction == "right":
        return "left"
    

    








