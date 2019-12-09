X = 99
# p 501


def maker(N):
    def action(X):
        return X ** N
    return action(X)


f = maker(5)

print(f)