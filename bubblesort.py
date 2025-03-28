import random
from random import randrange
print(randrange(10))

numbers = [randrange(10), randrange(10), randrange(10), randrange(10)]

print(numbers)

def sort(x):
    for i in range(len(x)):
        if i + 1 == len(x):
            print("At position " + str(i))
            print(x[i])
        else:
            print("At position " + str(i))
            print(x[i])
            print("Next position " + str(i + 1))
            print("Data at next position " + str(x[i + 1]))
        print("At position " + str(i))
        print(x[i])
        print("Next position " + str(i + 1))
        print("Data at next position " + str(x[i + 1]))

sort(numbers)
