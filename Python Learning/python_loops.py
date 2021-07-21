# Implement Python Loops for lists, tuples, and dictionaries ---------------
# players = ['Altuve', 'Bregman', 'Correa', 'Gattis'] # List

# for player in players:
#     print(player)

# players = ('Altuve', 'Bregman', 'Correa', 'Gattis') # Tuple

# for player in players:
#     print(player)

# players = { # Dictionary
#     '2b': 'Altuve',
#     '3b': 'Bregman',
#     'ss': 'Correa',
#     'dh': 'Gattis'
# }

# for position, player in players.items():
#     print('Position', position)
#     print('Player Name', player)

# ----------------------------------------------------

# alphabet = 'abcdef'

# for letter in alphabet:
#     print(letter)

# ----------------------------------------------------
# Looping over ranges
# for num in range(1, 11, 2):
#     print(num)

# ----------------------------------------------------
# Continue and Break
# usernames = [
#   'jon',
#   'tyrion',
#   'theon',
#   'cersei',
#   'sansa',
# ]

# for username in usernames:
#     if username == 'cersei':
#         print(f'Sorry, {username}, you are not allowed')
#         continue
#     else:
#         print(f'{username} is allowed')

# for username in usernames:
#     if username == 'cersei':
#         print(f'{username} was found at index{usernames.index(username)}')
#         break
#     print(username)

# def loop_and_break():
#     vegetables = ["onion", "broccoli", "apple", "spinich"]
#     for vegetable in vegetables:
#         if vegetable == 'apple':
#             print(f'{vegetable} is not a vegetable')
#             break
#         print(vegetables)