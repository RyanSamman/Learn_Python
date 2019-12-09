counters = [1, 2, 3, 4]

updated = []

for x in counters:
    updated.append(x + 10)

print(updated)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def inc(x): return x + 10


updated2 = list(map(inc, counters))
print(updated2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
run = lambda x: x + 10
updated3 = list(map(run, counters))  # map does a for loop for every item in counters, and appends it into
# updated3, [run(counters[0], run(counters[1]), etc
print(updated3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
power = lambda x, y: x ** y
print(list(map(power, [1, 2, 3], [2, 3, 4])))  # [power(1**2), power(2**3), etc p 574 to 576
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(list(filter(lambda y: y > 0, range(-5, 5))))  # if filter(x, y), when x is true y is appended p 576
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reduce p 577
from functools import reduce

summer = lambda y, z: y + z
list1 = [1, 2, 3, 4]

print(reduce(summer, list1))
# (((1 + 2) + 3) + 4)
# same as:


def myreduce(function, sequence):
    tally = sequence[0]  # Takes first index of list sequence and inserts it into the function
    for next in sequence[1:]:
        tally = function(tally, next) # Then puts it with the next and "recursion" until it ends
    return tally


print(myreduce(summer, list1))