import random 

door = ['a', 'b', 'c']
no_change = 0
change = 0

trial=100000

for _ in range(trial):
    car = random.randint(0,2)
    player_choice = random.randint(0,2)

    empty_door = []
     for i in range(3):
        if i!=player_choice and i != car:
            empty_door.append(door[i])

    com = random.sample(empty_door, 1)[0]

    if player_choice == car:
        no_change += 1

    empty_door.remove(com)

    if not empty_door:
        change +=1
print("선택을 바꾸지 않은 경우:", no_change/trial,"%")
print("선택을 바꾼 경우:", change/trial,"%")

