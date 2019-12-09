x = 4


def maker(N):
    return lambda X, N=N: X ** N


h = maker(3)

print(h)

print(h(4))
print(h(5))