def sumtree(L):
    total = 0
    for i in L:
        if isinstance(i, list):  # Returns True / False if i is (TYPE) p 558
            total += sumtree(i)
        else:
            total += i
    return total


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))

A = [0]
A.extend(L[1])  # p.559, adds onto list
print(A)