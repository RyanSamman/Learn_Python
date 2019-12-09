# Creating a list:
L = [123,"abc",1.23]                # Remember 0 is first, 1 is second, 2 is third etc..
print(L)                            # Negative numbers is same as length-n

# Indexing position
L[0]
print(L[0])

# Slicing (remember [:x] is up to but not including
L[:2]  # Prints 123 only
L[1:2] # Prints abc

# Addition to list
L + [456,"def"]
L.append(456) # adds to end of list
# L[2]= .... old items can be changed freely
# L[3]= ....  NEW ADDITION MUST BE NUMBER EXACTLY AFTER END OF LIST

# Removing from list
L.pop(0)  # Also print(L.pop(x) shows which item it removed
L.pop(1)

len(L) # To find length of list
L.count(123) # To count how many times (123) came in the list
L.index(123) # To see where 123 is (0,1,2,3...)

# Duplicating items in a list
L * 2

M = ["bb","aa","cc","qq"]
# Sorting list:
M.sort()  # In alphabetical order

M.reverse()  # Flips item's order in list (to sort and reverse, M.sort(reverse)

# You can nest a list in a list
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# to retrieve an item from the two lists
# M[x][y]
# M[x] is a row of the "Matrix"
row1 = M[0]
print(row1,'\n')

# To get a column:
col1 = [f[0] for f in M]    # f is every nested list item, so when you do f[0],
print(col1,'\n')            # it will select the first item of the nested list

# to get a diagonal:
diag = [M[i][i] for i in [0, 1, 2]] # diag = [M[0][0],M[1][1],M[2][2]]
print(diag,'\n')

X=list(range(0,21,5))  # range(start,end *EXCLUSION*, gap)
print(X)               # MUST HAVE list(range()) to make into list

Y = [[x, x ** 2, x ** 3] for x in range(4)]
print(Y)

Z = [[ i, i / 2, i ** 2] for i in range(-6,7,2) if i > 0]
print(Z)

G = (sum(row) for row in M)  # To make a generator
print(next(G))               # To get individual values
# See test1 for a loop to get all values calculated from a list

Sumrow = list(map(sum,M))  # As if it is converted into a string then calculated
# map(command, object)      # item by item in main list, then put back into a list
# Same as doing [sum(row) for row in M] shown in test1

############## Tuples ###################
# Used where the immutability is the point, used in more complex tasks
# Same as lists but cannot be edited after creation
T = (1,2,3,4,5) # Has () instead of [], the () can be ommited but when printing value it will show ()
T2 = 'spam', 3.0, [11,22,33]
print(T2)  # Indexing works the same as nested list etc..


len(T) # Same functions as list
T + (6,7)  # To extend     #MUST HAVE AT LEAST ONE ',' OR ERROR WILL APPEAR
T[0] # to index, slice etc
# T[1] = 5 wont work as it is a tuple data structure
# T.append(....) wont work either

# To edit, a new tuple must be created
T =(2,) + T[1:]























