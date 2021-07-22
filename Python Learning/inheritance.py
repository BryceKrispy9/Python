class User: # Elements (first name, last name)
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self): # Function
        return f'Hi {self.first_name} {self.last_name}'


class AdminUser(User):
    def active_users(self):
        return '500'


bryce = AdminUser('brycepearson09@gmail.com', 'Bryce', 'Pearson')

devyn = User('devyn.nelson@gmail.com', 'Devyn', 'Pearson')

print(bryce.active_users())
print(devyn.greeting())