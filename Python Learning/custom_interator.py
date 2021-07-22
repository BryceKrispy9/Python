class Lineup:
    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0 # Keep track of where we are in the astros lineup
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self): # See what n is (First it is 0)
        if self.n < self.last_player_index:  # Is it less than the list? Subtract 1 because we don't want the length of the list, we want the value of the index at the last element
            player = self.get_player(self.n)
            self.n += 1 # Increment by 1 (move down the line)
            return player
        elif self.n == self.last_player_index: # Conditional
            player = self.get_player(self.n)
            self.n = 0
            return player

astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))