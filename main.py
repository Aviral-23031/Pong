from turtle import Turtle,Screen
from paddle import Paddle
from MidLine import MidLine
from ball import Ball
import time

from score import Score

screen = Screen()
screen.setup(800,600)
screen.bgcolor("lawngreen")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
midline = MidLine()
ball = Ball()
score = Score()


screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_on =True



while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor() > 380:
        score.l_point()
        ball.reset()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset()


screen.exitonclick()