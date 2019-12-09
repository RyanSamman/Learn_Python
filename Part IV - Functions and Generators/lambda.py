def makeActions():
    acts = []
    for i in range(5):  # Makes list with indexes 0 to 4, then power of x
        acts.append(lambda x, i=i: i ** x)  # only remembers i from when it was made when nested, i=i inputs local
    return acts


# Page 507, i=i to iterate values
acts = makeActions()

# for
print(acts[3](4))

# Main benefit of lambda is to delay running of code until needed
# Read page 572 573 for more details

list1 = [(6, 7, 8), (9, 10, 11)]
list2 = []

for a, b, c in list1: # makes a list of different lambda functions
    list2.append(lambda x=a, y=b, z=c: x + y + z)  # Can be integrated into a list


print(list2)  # Code not run until called with ()
print(list2[1]())
print(list2[0](1, 2, 3))
