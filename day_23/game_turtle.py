from turtle import Turtle

POSITION = (0, -280)
MOVE = 10
HEADING = 90


class Game_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(POSITION)
        self.setheading(HEADING)
        self.difficulty = 0.1

    def move_up(self):
        self.forward(MOVE)

    def reset(self):
        self.goto(POSITION)
        self.difficulty *= 0.9
