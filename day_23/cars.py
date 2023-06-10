from turtle import Turtle


class Cars(Turtle):
    def __init__(self, position, colors):
        super().__init__()
        self.color((colors))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.y_cor = position[1]
        self.goto(position)
        print(position[1])

    def move(self):
        if self.xcor() < -310:
            self.goto(310, self.y_cor)
        self.backward(10)
