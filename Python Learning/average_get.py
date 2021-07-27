# import statistics (or functools > reduce)
# sum / total num of elements

# num_list = [1, 2, 3, 4, 5, 6]

# print(statistics.mean(num_list))

from functools import reduce

def get_average(num_list):
    total = reduce(
            (lambda total, element: total + element),
            num_list)

    return total / len(num_list)

num_list = [1, 2, 3, 4, 5, 6]

print(get_average(num_list))