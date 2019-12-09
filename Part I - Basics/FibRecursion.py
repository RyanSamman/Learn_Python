Fiblist = []


def fibbonachi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibbonachi(n-2) + fibbonachi(n-1)
    if n < 1:
        return "Error"


for i in range(0, 100):
    Fiblist.append(fibbonachi(i))
print(Fiblist)
