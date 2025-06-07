Players = {
    'Rohit': {'runs': 10000, 'centuries': 15},
    'Virat': {'runs': 12000, 'centuries': 18}
}
for player, stats in Players.items():
    print(player)
    for key, value in stats.items():
        print(f"{key} :\t {value}")