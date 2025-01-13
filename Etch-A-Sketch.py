from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.textinput("Welcome to Etch-A-Sketch", "WASD keys to move. To turn pen on and off, press 1 and two respectively. Press enter to continue")


def moveforward():
    tim.forward(10)
def movebackward():
    tim.forward(-10)
def leftturn():
    tim.left(5)
def rightturn():
    tim.right(5)
def stop_draw():
    tim.penup()
def continue_draw():
    tim.pendown()





screen.listen()
screen.onkeypress(key="w", fun=moveforward)
screen.onkeypress(key="s", fun=movebackward)
screen.onkeypress(key="a", fun=leftturn)
screen.onkeypress(key="d", fun=rightturn)
screen.onkeypress(key="1", fun= stop_draw)
screen.onkeypress(key="2", fun= continue_draw)














screen.exitonclick()