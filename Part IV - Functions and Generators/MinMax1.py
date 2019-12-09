def min1(*args):
    temp_max = args[0]
    for i in args:
        if i < temp_max:
            temp_max = i
    return temp_max


list = [5, 8, 16, 781, 71, 7, 1]

print(min1(*list))
