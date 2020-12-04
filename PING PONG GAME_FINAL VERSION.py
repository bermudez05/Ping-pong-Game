import turtle
import os

#Ping pong game
#Problems:main: paddle collision, computer movement pad...

def home_page():                            #Home page: "mantain game open"

    screen= turtle.Screen()
    screen.title("Pong game")
    screen.bgpic("intro_black.gif")
    screen.setup(width=700, height=500)

    turtle.listen()
    turtle.onkey(selection_c,"c")
    turtle.onkey(selection_p,"p")

def selection_c(): # Vs Computer mode game - still working on it. (there are some faults on the program -many-)

    player_1 = 0  # "Scorer"
    computer = 0

    turtle.clearscreen()                        #Events - controls player_1
    def down_player1():
        left_pad.sety(left_pad.ycor()-10)
        if left_pad.ycor()< -120.00:            #Make sure it doesn't cross the framework
            left_pad.sety(left_pad.ycor()+10)
    def up_player1():
        left_pad.sety(left_pad.ycor()+10)
        if left_pad.ycor()> 130.00:             #Make sure it doesn't cross the framework
            left_pad.sety(left_pad.ycor()-10)

    turtle.clearscreen()                        #Set screen
    screen= turtle.Screen()
    screen.bgcolor("White")
    screen.setup(width=700, height=500)

    framework = turtle.Turtle()                 #Unnecessary stuff add by me (simulate the gameboard)
    framework.speed(10)
    framework.up()
    framework.ht()
    framework.begin_fill()
    framework.fillcolor("black")
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

    left_pad = turtle.Turtle()                  #Left paddle - Player_1
    left_pad.penup()
    left_pad.shape("square")
    left_pad.color("white")
    left_pad.shapesize(stretch_wid=5, stretch_len=1)
    left_pad.goto(-250, 0) #Set intial position

    computer_pad = turtle.Turtle()              #Computer paddle
    computer_pad.penup()
    computer_pad.shape("square")
    computer_pad.color("white")
    computer_pad.shapesize(stretch_wid=5, stretch_len=1)
    computer_pad.goto(240, 0) #Set intial position
    computer_pad.y = -3 #Number 'of change on the movement' in the Y "axis"   - only vertical movemente on the paddle-

    ball = turtle.Turtle()                      #Ball
    ball.penup()
    ball.shape("circle")
    ball.color("white")
    ball.x = 2  #Number 'of change on the movement' in the X "axis"
    ball.y = -2  #Number 'of change on the movement' in the Y "axis"
    t = 1         # "Rate"
    speed_ind = 0 # "Index"


    score = turtle.Turtle()                     #Score write output
    score.up()
    score.ht()
    score.goto(0,190) #Set position
    score.write ('PLAYER_1 = 0    Vs    COMPUTER = 0',True,align="center",font=("comic sans",40,"normal"))

    turtle.listen()                             #Player_1 paddle movement
    turtle.onkey(down_player1,"Down")
    turtle.onkey(up_player1,"Up")

    while True:                                 #Start game "bucle"

        speed_ind = speed_ind + 1               #Ball movement in 2D (-for better understanding separate the movement cases in which the ball "bounce")
        turtle.update()
        ball.setx(ball.xcor()+(ball.x*t))       # *t == creates sort of an accelerated movement
        ball.sety(ball.ycor()+(ball.y*t))

        if speed_ind  > 500:                    #Works as a time index which indicates after what certain "change of position"/time the variable t should change
            speed_ind = 0
            if t < 15:                           # t<15 Avoid the movement of the ball going mad
                t = t + 0.2

        computer_pad.sety(computer_pad.ycor() + computer_pad.y)             #Computer pad movement.
        computer_pad.setx(computer_pad.xcor())                              #Computer pad movements - notes: looking for a rought game beetween player and computer
        if (computer_pad.ycor() > 130) or (computer_pad.ycor() < -120):     #I try to synchronize the movement of the paddle with the ball, in that case the
            computer_pad.y = computer_pad.y * -1                            #movement of the computer in the Y 'axis' will be given by the movement of the ball in Y
                                                                            #computer.sety(ball.ycor()) however this brings other problems along which by matter of
                                                                            #time I can't deal with right now (like the case when the computter paddle goes out the framework)
                                                                            #Vacation future problem! great!

        if ball.ycor() > 170:             #Movement of the ball in the "Y edges" of the framework
            ball.y = ball.y * -1          #Mental note. have in mind that the position does not look at all correct.
        if ball.ycor() < -160:
            ball.y = ball.y * -1          #Change ball direction (the posibles movements when the ball "bounce" will be illustrate in "Practice stuff")

        if ball.xcor() < -270:            #Movement of the ball in the "X edges" of the framework
            computer = computer + 1       #Score points.
            computer_pad.goto(240,0)      #Set paddles to initial position
            left_pad.goto(-250,0)
            ball.ht()
            ball.home()
            ball.st()
            ball.x = ball.x * -1         #Change ball direction (the posibles movements when the ball "bounce" will be illustrate in "Practice stuff")
            score.clear()
            score.goto(0,190)           #Update score and reset gameboard
            score.write ('PLAYER_1 = {}    Vs    COMPUTER = {}'.format(player_1,computer),True,align="center",font=("comic sans",40,"normal"))

        if ball.xcor() > 260:
            player_1 = player_1 + 1     #Score points.
            computer_pad.goto(240,0)    #Set paddles to initial position
            left_pad.goto(-250,0)
            ball.ht()
            ball.home()
            ball.st()
            ball.x = ball.x * -1        #Change ball direction (the posibles movements when the ball "bounce" will be illustrate in "Practice stuff")
            score.clear()
            score.goto(0,190)   #Update score and reset gameboard
            score.write ('PLAYER_1 = {}    Vs    COMPUTER = {}'.format(player_1,computer),True,align="center",font=("comic sans",40,"normal"))

        # left paddle collision    (Initial distance for collision == 50)
        if (ball.xcor() < -230) and (ball.ycor() > left_pad.ycor()-50 and ball.ycor() < left_pad.ycor()+50):
            #os.system("afplay pong_sound_effect.wav")  doesn't work... stops all the action while playing the sound
            #Vacation future problem! great!
            ball.x = ball.x * -1

        # right (computer) paddle collision
        if (ball.xcor() > 220) and (ball.ycor() > computer_pad.ycor()-50 and ball.ycor() < computer_pad.ycor()+50):
            #os.system("afplay pong_sound_effect.wav") doesn't work... stops all the action while playing the sound
            #Vacation future problem! great!
            ball.x = ball.x * -1

        #Ball and paddle collision: there still are some kind of crazy movements and situations on the collisions
        #I suspect that this ones come from the wrong area of collision of the paddle it doesn't work correctly on paddles corners
        #Vacation future problem! great!

        if (player_1 == 3) or (computer == 3):  #Rounds: number of points to end game == 3
            break                               #End game

    if player_1 == 3:                           #Player_1 wins, set screen!
        screen.bgpic("player_1black.gif")
        ball.reset()
        left_pad.reset()
        right_pad.reset()
        turtle.clearscreen()
    else:                                       #Computer wins, set screen!
        screen.bgpic("try again_black.gif")
        ball.reset()
        left_pad.reset()
        right_pad.reset()
        turtle.clearscreen()
        os.system("afplay lose.wav")            #First sound

    turtle.onkey(home_page,"space")

def selection_p():    #Two players game mode

    player_1 = 0    #"Scorer"
    player_2 = 0

    def down_player1():                         #Events - controls player_1
        left_pad.sety(left_pad.ycor()-8)
        if left_pad.ycor()< -120.00:            #Make sure it doesn't cross the framework
            left_pad.sety(left_pad.ycor()+8)
    def up_player1():
        left_pad.sety(left_pad.ycor()+8)
        if left_pad.ycor()> 130.00:             #Make sure it doesn't cross the framework
            left_pad.sety(left_pad.ycor()-8)
    def down_player2():                         #Events - controls player_2
        right_pad.sety(right_pad.ycor()-8)
        if right_pad.ycor()< -120.00:           #Make sure it doesn't cross the framework
            right_pad.sety(right_pad.ycor()+8)
    def up_player2():
        right_pad.sety(right_pad.ycor()+8)
        if right_pad.ycor()> 130.00:            #Make sure it doesn't cross the framework
            right_pad.sety(right_pad.ycor()-8)

    turtle.clearscreen()                        #Set screen
    screen= turtle.Screen()
    screen.bgcolor("White")
    screen.setup(width=700, height=500)

    framework = turtle.Turtle()                 #Unnecessary stuff add by me (simulate the gameboard)
    framework.speed(10)
    framework.up()
    framework.ht()
    framework.begin_fill()
    framework.fillcolor("black")
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

    left_pad = turtle.Turtle()                      #Left paddle - Player_1
    left_pad.penup()
    left_pad.shape("square")
    left_pad.color("white")
    left_pad.shapesize(stretch_wid=5, stretch_len=1)
    left_pad.goto(-250, 0)

    right_pad = turtle.Turtle()                     #Right paddle - Player_2
    right_pad.penup()
    right_pad.shape("square")
    right_pad.color("white")
    right_pad.shapesize(stretch_wid=5, stretch_len=1)
    right_pad.goto(240, 0)

    ball = turtle.Turtle()                         #Ball
    ball.penup()
    ball.shape("circle")
    ball.color("white")
    ball.x = 2  #Number 'of change on the movement' in the X "axis"
    ball.y = -2 #Number 'of change on the movement' in the Y "axis"
    t = 1       # "Rate"
    speed_ind = 0   # "Index"

    turtle.listen()                                 #Paddles movement (both players)
    turtle.onkey(down_player1,"s")
    turtle.onkey(up_player1,"w")
    turtle.onkey(down_player2,"Down")
    turtle.onkey(up_player2,"Up")

    score = turtle.Turtle()                        #Score write output
    score.up()
    score.ht()
    score.goto(0,190) #Set position
    score.write ('PLAYER_1 = 0    Vs    PLAYER_2 = 0',True,align="center",font=("comic sans",40,"normal"))


    while True:                                     #Start game "bucle"

        speed_ind = speed_ind + 1                   #Ball movement in 2D (-for better understanding separate the movement cases in which the ball "bounce")
        turtle.update()
        ball.setx(ball.xcor()+ (ball.x*t))          # *t == creates sort of an accelerated movement
        ball.sety(ball.ycor()+ (ball.y*t))

        if speed_ind  > 500:                        #Works as a time index which indicates after what certain "change of position"/time the variable t should change
            speed_ind = 0
            if t < 15:                              # t<15 Avoid the movement of the ball going mad
                t = t + 0.2

        if ball.ycor() > 170:                       #Movement of the ball in the "Y edges" of the framework
            ball.y = ball.y * -1                    #Mental note. have in mind that the position does not look at all correct.
        if ball.ycor() < -160:
            ball.y = ball.y * -1

        if ball.xcor() < -270:          #Movement of the ball in the "X edges" of the framework
            player_2 = player_2 + 1
            right_pad.goto(240, 0)
            left_pad.goto(-250, 0)
            ball.ht()
            ball.home()
            ball.st()
            ball.x = ball.x * -1                    #Change ball direction (the posibles movements when the ball "bounce" will be illustrate in "Practice stuff")
            t = 1
            score.clear()
            score.goto(0,190)                      #Update score and reset gameboard
            score.write ('PLAYER_1 = {}    Vs    PLAYER_2 = {}'.format(player_1,player_2),True,align="center",font=("comic sans",40,"normal"))

        if ball.xcor() > 260:
            player_1 = player_1 + 1
            right_pad.goto(240, 0)
            left_pad.goto(-250, 0)
            ball.ht()
            ball.home()
            ball.st()
            ball.x = ball.x * -1                    #Change ball direction (the posibles movements when the ball "bounce" will be illustrate in "Practice stuff")
            t = 1
            score.clear()
            score.goto(0,190)                       #Update score and reset gameboard
            score.write ('PLAYER_1 = {}    Vs    PLAYER_2 = {}'.format(player_1,player_2),True,align="center",font=("comic sans",40,"normal"))

        # Left paddle collision    (Initial distance for collision == 50)
        if (ball.xcor() < -230) and (ball.ycor() > left_pad.ycor()-50 and ball.ycor() < left_pad.ycor()+50):
            #os.system("afplay pong_sound_effect.wav")  doesn't work... stops all the action while playing the sound
            #Vacation future problem! great!
            ball.x = ball.x * -1

        # Right paddle collision
        if (ball.xcor() > 220) and (ball.ycor() > right_pad.ycor()-50 and ball.ycor() < right_pad.ycor()+50):
            #os.system("afplay pong_sound_effect.wav") doesn't work... stops all the action while playing the sound
            #Vacation future problem! great!
            ball.x = ball.x * -1

        #Ball and paddle collision: there still are some kind of crazy movements and situations on the collisions
        #I suspect that this ones come from the wrong area of collision of the paddle it doesn't work correctly on paddles corners
        #Vacation future problem! great!

        if (player_1 == 3) or (player_2 == 3):          #Rounds: number of points to end game == 3
            break                                       #End game

    if player_1 == 3:                                   #Player_1 wins, set screen!
        turtle.clearscreen()
        screen.bgpic("player_1black.gif")
        ball.reset()
        left_pad.reset()
        right_pad.reset()

    else:                                               #Player_2 wins, set screen!
        turtle.clearscreen()
        screen.bgpic("player_2black.gif")
        ball.reset()
        left_pad.reset()
        right_pad.reset()

    turtle.onkey(home_page,"space")

screen= turtle.Screen()             #Initial "home page"
screen.bgcolor('BLack')
screen.title("Pong game")
screen.bgpic("intro_black.gif")
screen.setup(width=700, height=500)

turtle.listen()                     #Selection mode
turtle.onkey(selection_c,"c")
turtle.onkey(selection_p,"p")

turtle.exitonclick()
