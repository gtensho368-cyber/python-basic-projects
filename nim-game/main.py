
import stones

start_stones = stones.initialize()
user_turn = True

while start_stones > 0:
    print(stones.show_game(start_stones))

    if user_turn:
        removed = stones.user_pick()
    else:
        removed = stones.computer_pick(start_stones)
        print(f"The computer picked {removed} stones.")

    start_stones -= removed
    user_turn = not user_turn

if user_turn:
    print("The computer picked the last stone.")
else:
    print("The player  picked the last stone.")    




















