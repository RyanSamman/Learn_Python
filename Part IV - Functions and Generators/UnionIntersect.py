list1 = range(0, 11)
list2 = range(-5, 6)


def union(args1, args2):
    union_list = []
    for i in args1:
        union_list.append(i)
    for i in args2:
        if i not in args1:
            union_list.append(i)
    return sorted(union_list)


def intersection(args1, args2):
    intersection_list = []
    for i in args1:
        if i in args2:
            intersection_list.append(i)
    return sorted(intersection_list)


print(union(list1, list2), intersection(list1, list2), sep="\n")
