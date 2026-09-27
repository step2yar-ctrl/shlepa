
players = [
    ["Alex", 1200],
    ["Max", 850],
    ["John", 1500],
    ["Katy", 1000]
]


get_rating = lambda player: player[0]
sorted_players = sorted(players, key=get_rating)
print(sorted_players)