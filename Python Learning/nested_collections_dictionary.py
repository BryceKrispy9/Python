teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
}

# print(teams['astros'][:2])

# astros = teams["astros"]
# print(teams["angels"])
# print(teams["astros"])
# print(teams["yankees"])

# teams['red sox'] = ["Price", 'Betts']

featured_team = teams.get('mets', 'No featured team')

# featured_team = teams.get('yankees', 'No featured team')

print(featured_team)