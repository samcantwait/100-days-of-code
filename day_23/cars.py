from turtle import Turtle
import random

NUMBER_OF_CARS = 20

def rand_x():
    return random.randrange(-300, 300, 20)

def rand_y(): 
    return random.randrange(-250, 250, 30)

def rand_color():
    colors = []
    for _ in range(3):
        colors.append(random.randint(0, 255))
    return tuple(colors)

class Cars:
    def __init__(self):
        self.all_cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(NUMBER_OF_CARS):
            new_car = Turtle('square')
            new_car.color(rand_color())
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(rand_x(), rand_y())
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if car.xcor() < -310:
                car.goto(310, rand_y())
            car.backward(10)
