
    for i in range(3):
        if i!=player_choice and i != car:
            empty_door.append(door[i])

    com = random.sample(empty_door, 1)[0]
