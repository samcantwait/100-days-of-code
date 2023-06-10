import random
import time
from turtle import Screen
from game_turtle import Game_turtle
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)
screen.colormode(255)

game_turtle = Game_turtle()
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
    time.sleep(0.1)  # change this to variable
    screen.update()
    for car in range(len(cars)):
        cars[car].move()
    if game_turtle.ycor() >= 290:
        game_turtle.reset()
        # increase move speed of cars

screen.exitonclick()
