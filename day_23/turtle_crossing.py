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
cars = []
for _ in range(20):
    position = (random.randint(-300, 300), random.randint(-250, 250))

    def color():
        return random.randint(0, 255)
    colors = (color(), color(), color())
    car = Cars(position, colors)
    cars.append(car)

screen.listen()
screen.onkeypress(game_turtle.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(game_turtle.difficulty) 
    screen.update()
    for car in range(len(cars)):
        if game_turtle.distance(cars[car]) < 35 and (game_turtle.ycor() > cars[car].ycor() - 20 and game_turtle.ycor() < cars[car].ycor() + 20):
            game_is_on = False
        cars[car].move()

    if game_turtle.ycor() >= 290:
        game_turtle.reset()
        scoreboard.increase_level()
    if not game_is_on:
        scoreboard.game_over()
        

screen.exitonclick()
