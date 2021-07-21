# List: []
# Dictionary: {}
# Tuple ()

# Tuple: immutable
# List: mutable

# post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content')

# title, sub_heading, content = post # Tuple

# title = post[0]
# sub_heading = post[1]
# content = post[2]
# ^ Lists

# print(title)
# print(sub_heading)
# print(content)

# ------------------------------------------------ Adding to a tuple

# post = post + ('published') -> Does not work

# print(id(post)) # ID in memory
# print(id(post))

# post += ('published',)

# print(id(post))

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)

# ------------------------------------------------ Nesting a tuple with a list inside

# tags = ['python', 'coding', 'tutorial']

# post += (tags,)

# print(post[-1][1])

# ------------------------------------------------ Slices

# print(post[1::2])

# ------------------------------------------------ Remove elements

post = ('Python Basics', 'Intro guide to Python', 'Some cool Python content', 'published')

# Removing elements from end
# post = post[:-1]

# Removing elements from the beginning
# post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)