from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self, position, colors):
        super().__init__()
        self.color((colors))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.y_cor = position[1]
        self.goto(position)

    def move(self):
        if self.xcor() < -310:
            self.goto(310, random.randint(-250, 250))
        self.backward(10)
