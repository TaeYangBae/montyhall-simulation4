import random 

door = ['a', 'b', 'c']
no_change = 0
change = 0

trial=100000

for _ in range(trial):
    car = random.randint(0,2)
    player_choice = random.randint(0,2)

    empty_door = []
