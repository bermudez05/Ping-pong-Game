import turtle
# Write on Turtle

# Home page..
screen= turtle.Screen()
screen.title("Pong game")
screen.setup(width=700, height=500)

a = 34
b = 35
score = turtle.Turtle()
score.up()
score.ht()
score.goto(0,190)
score.write ('PLAYER_1 = {}    Vs    PLAYER 2 = {}'.format(a,b),True,align="center",font=("comic sans",40,"normal"))

turtle.done()
