from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.get_high_score();
        self.update_scoreboard()

    def get_high_score(self):
        with open('day_20-21/data.txt') as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        with open('day_20-21/data.txt', mode='w') as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()