from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PINGYPONGY")
screen.tracer(0)
screen.setup(800, 600)

paddleL = Paddle((-350,0))
paddleR = Paddle((350,0))
ball=Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(paddleR.up, "Up")
screen.onkeypress(paddleR.down, "Down")

screen.onkeypress(paddleL.up, "w")

screen.onkeypress(paddleL.down, "s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detecting collision with paddle
    if (ball.xcor() > 325 or ball.xcor()< -325) and (ball.distance(paddleR) < 45 or ball.distance(paddleL)< 45 ):
        ball.bounce_with_paddle()

    if ball.xcor() > 380:
        print("Missed by right")
        scoreboard.point_left()
        ball.reset_position()

    if ball.xcor() < -380:
        print("Missed by left")
        scoreboard.point_right()

        ball.reset_position()

screen.exitonclick()
