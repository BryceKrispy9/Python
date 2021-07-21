players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

# print(players.keys())

# print(players.values())

# print(list(players.values())[1])

# print(players.items())

# player_names = list(players.copy().values())

# print(player_names)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

# print(len(team_groupings))

# print(team_groupings)

# print(list(team_groupings))

print(list(team_groupings)[1][1][0])