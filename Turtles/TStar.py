import turtle

turtle.speed(1)




turtle.bgcolor("Black")
turtle.pensize(2)

turtle.speed(1)
turtle.pendown()
turtle.color("Yellow", "Yellow")
turtle.begin_fill()

for i in range(5):
    turtle.forward(150)
    turtle.right(144)

turtle.speed(1)

turtle.end_fill()
turtle.hideturtle()
turtle.done()


