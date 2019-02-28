
import random

def prefix_sum(an_array):
    # len N, each element is 0
    result = []
    for i in range(0,len(an_array)):
        if i == 0:
            result += an_array[0]

    return result

a = range(random.randint(50,100))
print(a)
print(prefix_sum(a))