import turtle
# Game mode selection

game_mode = -1 # if game_mode == 1 then it is against the computer, while game_mode == 0 is a game for 2 players.
# Home page..
screen= turtle.Screen()
screen.title("Pong game")
screen.bgpic("intro.gif")
screen.setup(width=700, height=500)
def selection_c():
    turtle.clearscreen()
    game_mode = 1
def selection_p():
    turtle.clearscreen()
    game_mode = 0
turtle.listen()
turtle.onkey(selection_c,"c")
