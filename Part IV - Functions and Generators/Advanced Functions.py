def function_one(a: int = 6) -> str:  # a is annotated as an integer, and the return is annotated as a str, p567
    b = 7
    return b * a  # gives no error just highlights due to annotated


echo = function_one  # x can reference func as well
print()

schedule = [ (echo, 5), (echo, "40")]

for (funct1, numb) in schedule:  # you can reference tuples
    print(funct1(numb))  # and process them

print(echo.__name__)  # Prints name of function
# print(dir(echo))
# print(dir(echo.__code__))

# Page 561 to 565
# ^ read __code__.co_varnames and .co_argcount

#  .__annotations__

function_one.count = 5

print(function_one('spam'))

# to see function attributes:
print(function_one.__annotations__)  # Can be used later to screen input
