

import turtle

import os
from pathlib import Path


if os.path.exists(str(Path.home()) + "\Documents\Pong"):
    print("Folder Exists")
else:
    os.mkdir(str(Path.home()) + "\Documents\Pong", 0o666)
    f = open(str(Path.home()) + "\Documents\Pong\High score.txt","x")
    f = open(str(Path.home()) + "\Documents\Pong\High score.txt", "w")
    f.write("0")

wn = turtle.Screen()
wn.title("Pong by The Mastermind")
wn.bgcolor("white")
wn.bgpic("Pong_Img/Untitled.png")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#box = turtle.Turtle()
#box.shape("square")
#box.shapesize(stretch_wid=40,stretch_len=30)
#box.penup()
#box.goto(0, 0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
f = open(str(Path.home()) + "\Documents\Pong\High score.txt", "r")
hs = f.read(100)
pen.write("Player A: 0  Player B: 0  High score: " + hs, align="center", font=("Courier", 20, "normal"))
f.close()





#Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()
    #paddle_b.ycor = ball.ycor

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if paddle_a.ycor() > 215:
        paddle_a.sety(215)
    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)
    if paddle_b.ycor() > 215:
        paddle_b.sety(215)
    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    #Boarder check
    if ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    #Player A score
    if ball.xcor() > 390:

        ball.dx = 0.15
        ball.dy = 0.15
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a += 1
        f = open(str(Path.home()) + "\Documents\Pong\High score.txt", "r")
        hs = f.read(100)
        if score_a > int(hs):
            b = open(str(Path.home()) + "\Documents\Pong\High score.txt", "w")
            b.truncate(0)
            b.write(str(score_a))
            b.close()

        f.close()
        g = open(str(Path.home()) + "\Documents\Pong\High score.txt", "r")
        hs = g.read(100)
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b) + " High score: " + hs, align="center",font=("Courier", 24, "normal"))
        f.close()
        print("Player A score: " + str(score_a) +"Player B score: " + str(score_b))


    #Player B score
    if ball.xcor() < -390:
        ball.dx = 0.15
        ball.dy = 0.15
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b += 1
        f = open(str(Path.home()) + "\Documents\Pong\High score.txt", "r")
        hs = f.read(100)
        if score_b > int(hs):
            b = open(str(Path.home()) + "\Documents\Pong\High score.txt", "w")
            b.truncate(0)
            b.write(str(score_b))
            b.close()
        f = open(str(Path.home()) + "\Documents\Pong\High score.txt", "r")
        hs = f.read(100)
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b) + " High score: " + hs, align="center",     font=("Courier", 24, "normal"))
        f.close()
        print("Player A score: " + str(score_a) +"Player B score: " + str(score_b))



    # paddle colider

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx += ball.dx/8
        ball.dx *= -1



    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx += ball.dx / 8
        ball.dx *= -1



