from turtle import Screen
import time
from scoreboard import Scoreboard
from paddles import Paddle
from ball import Ball

screen = Screen()
score = Scoreboard()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()


screen.listen()
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    """detect collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """detect collision with right paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """detect ball misses r_paddle"""
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    """detect ball misses l_paddle"""
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
