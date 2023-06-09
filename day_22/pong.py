from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, 'Up')
screen.onkeypress(right_paddle.go_down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() == 330 or ball.distance(left_paddle) < 50 and ball.xcor() == -330:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() >= 400:
        ball.reset()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() <= -400:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
