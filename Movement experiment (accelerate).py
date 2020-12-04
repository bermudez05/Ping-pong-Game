import turtle
# Movement experiment

screen = turtle.Screen()
screen.setup(width=500,height=400)
screen.bgcolor("white")


b = turtle.Turtle()
b.shape("circle")
b.dx = 0.1
b.dy = -0.1
t = 1
while True:
    t += 1
    b.sety((b.ycor()+(b.dy*t))/2)
    b.setx(b.xcor()+(b.dx*t)/2)
    print (t)
turtle.done()
