FibList = []


def fibbonachi(n):
    if len(FibList) - 1 >= n:
        return FibList[n]
    elif n == 0:
        FibList.append(0)
        return 0
    elif n == 1:
        FibList.append(1)
        return 1
    elif n > 1:
        x = fibbonachi(n-2) + fibbonachi(n-1)
        FibList.append(x)
        return x
    else:
        return "Error"


print(fibbonachi(4))
print(FibList)
print(fibbonachi(20))
print(FibList)
