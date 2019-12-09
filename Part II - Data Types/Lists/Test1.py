# To loop a generator until all results are shown
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Z = [sum(row) for row in M]  # Made into a list with [    ]

G = (sum(row) for row in M)  # Made into a generator w. (     )

Y = 0

while Y < len(Z):
    print(next(G))
    Y = Y + 1

############################
print('#')
Q = [sum(row) for row in M]

W = list(map(sum, M))

print(Q, W)

L = [ord(x) for x in 'spaam']  # List
S = {ord(x) for x in 'spaam'}  # Set
D = {x: ord(x) for x in 'spaam'}  # Dictionary
G = (ord(x) for x in 'spaam')  # Generator
print('List:', L, '\n\n', 'Set:', S, '\n\n', 'Dictionary:', D, '\n\n', 'Generator:', G)
