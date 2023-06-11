import random
import time
from turtle import Screen
from game_turtle import Game_turtle
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)
screen.colormode(255)

game_turtle = Game_turtle()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkeypress(game_turtle.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(game_turtle.difficulty) 
    cars.move()
    screen.update()
    for car in cars.all_cars:
        if game_turtle.distance(car) < 35 and (game_turtle.ycor() > car.ycor() - 20 and game_turtle.ycor() < car.ycor() + 20):
            game_is_on = False
    if game_turtle.crossed():
        game_turtle.reset()
        scoreboard.increase_level()
    if not game_is_on:
        scoreboard.game_over()
        

screen.exitonclick()
