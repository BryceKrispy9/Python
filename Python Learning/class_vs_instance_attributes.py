# Instance attributes - Belongs to the instance. We have to pass a new value every time.
# class Website:
#     def __init__(self, title):
#         self.title = title


# ws = Website('My Website Title')
# print(ws.__dict__)

# ws_two = Website('Second Title')
# print(ws_two.__dict__)


# Class attributes - Difference comes down to the name. Belongs to the class defition
class DifferentWebsite:
    title = 'My class title' # Belongs to the class (hardcoded)


dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)