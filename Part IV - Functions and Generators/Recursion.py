import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
# P 561

lower = (lambda x, y: x if x < y else y)

print(lower('bb', 'aa'))
print(lower('aa', 'bb'))

print('spam' < 'spa')
