# class Invoice():

#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

#     def formattor(self):
#         return f'{self.client} owes: ${self.total}'


# google = Invoice('Google', 100)
# snapchat = Invoice('Snapchat', 200)

# print(google.formattor())
# print(snapchat.formattor())

class Garage:
  
  def __init__(self, size):
      self.size = size

  def open_door(self):
    return "The door opens"
    
home = Garage(2) 