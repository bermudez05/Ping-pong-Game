import turtle
import random
# Intro for events

nic = turtle.Turtle()
nic.speed(10)
nic.width(5)

colors = ["yellow","blue","red","black"]

# events
def up():
    nic.setheading(90)
    nic.fd(100)
def down():
    nic.setheading(270)
    nic.fd(100)
def right():
    nic.setheading(0)
    nic.fd(100)
def left():
    nic.setheading(180)
    nic.fd(100)
def clickleft (x,y):
    nic.color(random.choice(colors))
def clickright (x,y):
    nic.stamp()

#listening for events / we are now listening for events
turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 2)

turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")

turtle.mainloop()
