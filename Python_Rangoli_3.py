import turtle
potti = turtle.Turtle()
potti.speed(500)
for i in range(180):
    potti.forward(100)
    potti.right(30)
    potti.forward(20)
    potti.left(60)
    potti.forward(50)
    potti.right(30)

    potti.penup()
    potti.setposition(0, 0)
    potti.pendown()

    potti.right(2)

turtle.done()