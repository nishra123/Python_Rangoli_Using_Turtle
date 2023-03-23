import turtle
t = turtle.Turtle()
babu = ["purple", "red", "orange", "blue", "green", "yellow"]
turtle.bgcolor("black")
for i in range(200):
    t.color(babu[i % 6])                    #if we take 1 instead of i in gthis line, prog will generate only red colour spiral
    t.pensize(i / 100 + 1)
    t.forward(i)
    t.left(59)

