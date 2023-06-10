from turtle import Turtle


class Game_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)
