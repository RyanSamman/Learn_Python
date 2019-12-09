def f_default(a, b=2000, c=3000):
    print(a, b, c)


# Here, a is a must to be called, however b and c is optional with a default value of b - 2 and c = 3 p533
# Read page 530 for types of function calling

f_default(1, c=3, b=2)  # order doesnt matter if a is given a value
f_default(c=5, b=10, a=3)


def f_set(a, b, c):
    print(a, b, c)


set1 = [5, 6, 7]
f_set(*set1)  # Makes items in set into the variables a, b, c


def f_dict(a, b, c=0):
    print(a, b, c)


dict1 = {"a": "10", "b": "Hello"}
f_dict(**dict1)  # Makes values of keys into the variables a, b, c (value of key a into a etc...)


def set2(*args):  # Makes inserted values into a tuple
    print(args)


set2(5, 6, 7, "Potato")


def dict2(**kwargs):  # Makes inserted values into a Dictionary
    print(kwargs)


dict2(a=5, b=6)
