import turtle

turtle.bgcolor("Black")
turtle.pensize(2)

turtle.speed(1)
turtle.pendown()
turtle.color("Red", "Red")
turtle.begin_fill()
input()
turtle.left(140)
turtle.forward(116.5)

turtle.speed(0)

for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.left(120)

for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.speed(1)

turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()



