import turtle
import collision
import os
from pathlib import Path


wn = turtle.Screen()
wn.title("PacMan by The Mastermind")
wn.bgcolor("black")

wn.tracer(0)
wn.setup(width=1.0, height=1.0)
screenTk = wn.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)



pac_man = turtle.Turtle()
pac_man.speed(0)
pac_man.shape("square")
pac_man.color("white")
pac_man.penup()
pac_man.goto(0, 0)

wall_1 = turtle.Turtle()
wall_1.speed(0)
wall_1.shape("square")
wall_1.color("white")
wall_1.penup()
wall_1.goto(0, 100)
#wall_1.shapesize(stretch_len= 50)

def moveUp():
    pac_man.setheading(90)
    pac_man.forward(10)
def moveDown():
    pac_man.setheading(270)
    pac_man.forward(10)
def moveLeft():
    pac_man.setheading(180)
    pac_man.forward(10)
def moveRight():
    pac_man.setheading(0)
    pac_man.forward(10)



while True:
    wn.update()

    wn.listen()
    wn.onkeypress(moveUp, "w")
    wn.onkeypress(moveDown, "s")
    wn.onkeypress(moveLeft, "a")
    wn.onkeypress(moveRight, "d")
    if pac_man.xcor() == wall_1.xcor() and pac_man.ycor() == wall_1.ycor():
    

    #if  pac_man.ycor() < wall_1.ycor() + 40 and pac_man.ycor() > wall_1.ycor() - 40 and pac_man.xcor() < wall_1.xcor() + 40 and pac_man.xcor() > wall_1.ycor() - 40:
      #  pac_man.sety(wall_1.ycor() + 40)




