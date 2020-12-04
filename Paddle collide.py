import turtle
# Paddle collide

player_1 = 0
player_2 = 0

# events/controls
def down_player1():
    left_pad.sety(left_pad.ycor()-7)
    if left_pad.ycor()< -120.00:            #Make sure it doesn't cross the framework
        left_pad.sety(left_pad.ycor()+7)
def up_player1():
    left_pad.sety(left_pad.ycor()+7)
    if left_pad.ycor()> 130.00:             #Make sure it doesn't cross the framework
        left_pad.sety(left_pad.ycor()-7)
def down_player2():
    right_pad.sety(right_pad.ycor()-5)
    if right_pad.ycor()< -120.00:           #Make sure it doesn't cross the framework
        right_pad.sety(right_pad.ycor()+7)
def up_player2():
    right_pad.sety(right_pad.ycor()+7)
    if right_pad.ycor()> 130.00:            #Make sure it doesn't cross the framework
        right_pad.sety(right_pad.ycor()-7)

# set screen
turtle.clearscreen()
screen= turtle.Screen()
screen.bgcolor("White")
screen.setup(width=700, height=500)

# unnecessary stuff add by me
framework = turtle.Turtle()
framework.up()
framework.ht()
framework.pencolor("black")
framework.begin_fill()
framework.fillcolor("#ACC7E9")
framework.speed(3)
framework.setpos(-290,180)
framework.down()
framework.fd(570)
framework.setheading(270)
framework.fd(350)
framework.setheading(180)
framework.fd(570)
framework.setheading(90)
framework.fd(350)
framework.end_fill()

# Left paddle
left_pad = turtle.Turtle()
left_pad.penup()
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=5, stretch_len=1)
left_pad.goto(-250, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.penup()
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=5, stretch_len=1)
right_pad.goto(240, 0)

# Ball of circle shape
ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("#3E5081")
ball.x = 2.5
ball.y = -2.5

# paddles movement (both players)
turtle.listen()
turtle.onkey(down_player1,"Down")
turtle.onkey(up_player1,"Up")
turtle.onkey(down_player2,"s")
turtle.onkey(up_player2,"w")

while True:

    #turtle.update()
    ball.setx(ball.xcor()+ ball.x)
    ball.sety(ball.ycor()+ ball.y)

    # bordes en el eje y            # para que visualmente se vea el toque con el Framework, le disminuimos a las cordenadas inciales.
    if ball.ycor() > 170:
        ball.y = ball.y * -1
    if ball.ycor() < -160:
        ball.y = ball.y * -1

    # bordes en el eje x
    if ball.xcor() < -280:
        player_2 = player_2 + 1
        ball.ht()
        ball.home()
        ball.st()
        ball.x = ball.x * -1

    if ball.xcor() > 270:
        player_1 = player_1 + 1
        ball.ht()
        ball.home()
        ball.st()
        ball.x = ball.x * -1

    # left paddle collision
    if (ball.xcor() < -230) and (ball.ycor() > left_pad.ycor()-50 and ball.ycor() < left_pad.ycor()+50):
        ball.x = ball.x * -1

    # right paddle collision
    if (ball.xcor() > 220) and (ball.ycor() > right_pad.ycor()-50 and ball.ycor() < right_pad.ycor()+50):
        ball.x = ball.x * -1

    # Rounds
    if (player_1 == 3) or (player_2 == 3):
        break

if player_1 == 3:
    ball.reset()
    left_pad.reset()
    right_pad.reset()
    turtle.clearscreen()
    screen.bgpic("player_1wins.gif")
else:
    ball.reset()
    left_pad.reset()
    right_pad.reset()
    turtle.clearscreen()
    screen.bgpic("player_2wins.gif")

turtle.exitonclick()
