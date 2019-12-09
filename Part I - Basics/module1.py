y = "Yes"
x = 0
while y == "Yes":

    print("Hello")
    x = eval(input("Insert a number: "))

    if x == 0:
        print("Zero")
    elif x > 0:
        print("Greater than Zero")
    elif x < 0:
        print("Less than Zero")
    else:
        print("Not a number")


    y = input("Continue? (Yes) ")
