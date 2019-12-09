def main():
    global y

    def play():
        nonlocal x
        x = 6
        y = 6
        z = 6

    x = 7
    y = 7
    z = 7
    play()
    print("X is", x)
    pass

z = 8
main()
print("Y is", y)
print("Z is", z)