import turtle
import random
turtle.bgcolor('black')
turtle.speed(100)
turtle.hideturtle()
x=10

def l():
    turtle.fd(x)
    turtle.right(90)
    turtle.fd(x)
    turtle.right(90)
    turtle.fd(x)
    turtle.right(90)
    turtle.fd(x)
    turtle.right(95)
f=0
while f < 72:
    l()
    turtle.pencolor("#%06x" % random.randint(0, 0xFFFFFF))
    if x < 215.3:
        x += 1.05
    elif x > 215.3:
        x += 0
        f += 1
