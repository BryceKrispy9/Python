teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# del teams['astros']

removed_team = teams.pop('mets', 'No team found by that name')

# removed_team = teams.pop('yankees', 'No team found by that name')

print(removed_team)