import random
from random import randrange

numbers = [randrange(10), randrange(10), randrange(10), randrange(10)]

print(numbers)

def check_sorted(x):
    sorted_count = 0
    for i in range(len(x)):
        if i + 1 == len(x):
            break
        else:
            if x[i] < x[i + 1] or x[i] == x[i + 1]:
                sorted_count = sorted_count + 1
    if sorted_count + 1 == len(x):
        return True
    else:
        return False


def sort(x):
    is_sorted = check_sorted(x)
    if is_sorted == True:
        return True
    else:
            for n in range(len(x) - 1, 0, -1):
                for i in range(n):
                    if x[i] > x[i + 1]:
                        x[i], x[i + 1] = x[i + 1], x[i]

sort(numbers)
print(numbers)
