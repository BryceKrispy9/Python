# def greeting(*args):
    # print('Hi ' + ' '.join(args))
    # print(args) # Tuples

def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}.")


# greeting('Bryce', 'Pearson')
# greeting('Bryce', 'Ben', 'Pearson')

greeting('morning', 'Bryce', 'Pearson')
greeting('afternoon', 'Bryce', 'Ben', 'Pearson')