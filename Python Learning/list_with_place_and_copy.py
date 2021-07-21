tags = ['python', 'development', 'tutortials', 'code']

# Nope
# tags[-1] = 'programming'
# tags.extend('programming')

# Yes
# tags.extend(['programming']) # Using a function

new_tags = tags + ['programming'] # Best practice method

print(new_tags)

print(tags)