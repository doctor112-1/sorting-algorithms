import random
from random import randrange

numbers = [randrange(10), randrange(10), randrange(10), randrange(10)]

save = numbers

test_sorted_array = [1, 3, 6, 9]

sorted_array = []

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
            for i in range(len(x)):
                if i + 1 == len(x):
                    print("At position " + str(i))
                    print(x[i])
                else:
                    if x[i] < x[i + 1]:
                        print("smaller than other")
                    elif x[i] > x[i + 1]:
                        print("bigger than other")
                        temp = x[i]
                        temp1 = x[i + 1]
                        x[i] = temp1
                        x[i + 1] = temp
                        print(x)
                    elif x[i] == x[i + 1]:
                        print("equal to other")
    sort(x)

sort(numbers)

print(numbers)
print(save)
