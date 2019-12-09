import sys
import json


def dir1(x):
    """
    Test! Test!
    :param x:
    :return:
    """
    for a in dir(x):
        if not a.__contains__("_"):  # or .startswith
            print(a, end=", ")


# print(dir1.__doc__)  # outputs the comments inside the function, can work with anything P446
# help(dir1)  # More info on help than .__doc__ p 449

# on cmd do : to release a webpage of documentation p 452
# py -m pydoc -b
