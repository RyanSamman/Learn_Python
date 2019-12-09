y = "Yes"
while y == "Yes":
    from math import sqrt
    num1 = eval(input("Enter first number: "))
    operation = input("(+,-,*,/,^ (Power),% (sqrt))\nEnter Operation type: ")
    if operation == "%":
        print(sqrt(num1))
    else:
        num2 = eval(input("Enter another number: "))
        y = "Yes"

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            print(num1 / num2)
        elif operation == "^":
            print(num1 ** num2)
        elif operation == "%":
            print(num1 - num2)
        else:
            print("Error")

    y = input("Continue? (Yes) ")

