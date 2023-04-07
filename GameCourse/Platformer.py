import time
import turtle

import os
from pathlib import Path


is_grounded = False
up = False
import time

jumping = False
gravity = -0.6

wn = turtle.Screen()
wn.title("Platformer test")
wn.bgcolor("black")
wn.setup(width=1400, height=750)
wn.tracer(0)

#Player
player = turtle.Turtle();
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, 0)
player.dx = 0
player.dy = 0

#Ground

ground = turtle.Turtle()
ground.speed(0)
ground.shape("square")
ground.color("white")
ground.penup()
ground.shapesize(stretch_wid=37.5, stretch_len=70)
ground.goto(0, -675)


def move_player_right():
    player.dx = 0.5
def stop_move_player_right():
    player.dx = 0

def move_player_left():
    player.dx = -0.5
def stop_move_player_left():
    player.dx = 0



#jump
def move_player_jump():
    
        player.dy = 0.6



while True:
    wn.update()
    print(player.dy)
    player.setx(player.xcor() + player.dx)
    player.sety(player.ycor() + player.dy)
   # print(jumping)
    if player.ycor() <= -290:
        player.dy = 0
    if player.ycor() > -290:
        player.dy = -0.6


    wn.listen()
    wn.onkeypress(move_player_right, "d")
    wn.onkeyrelease(stop_move_player_right, "d")
    wn.onkeypress(move_player_left, "a")
    wn.onkeypress(move_player_jump, "space")

    wn.onkeyrelease(stop_move_player_left, "a")









