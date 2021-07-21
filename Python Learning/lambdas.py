# full_name = lambda first, last: f'{first} {last}'

# print(full_name('Bryce', 'Pearson'))

# def greeting(name):
#     print(f'Hi there {name}')


# greeting(full_name('Bryce', 'Pearson'))


def lambda_practice(name):
    greeting = lambda name: f'{name}'
    print(f'Hi, {name}')
    
    
    return greeting

lambda_practice(name = 'Jordan')