from turtle import Screen, Turtle
import random
screen = Screen()
screen.setup(1200, 600)
screen.colormode(255)

rgb_colors = [(216, 176, 13), (188, 80, 22), (23, 125, 163), (220, 158, 93), (93, 37, 2), (172, 26, 11), (3, 116, 73), (31, 124, 82), (17, 42, 76), (243, 204, 208), (169, 53, 67), (240, 202, 4), (238, 204, 67)]

doodle = Turtle()
doodle.shape('turtle')
doodle.speed('fastest')
doodle.penup()
doodle.setpos(-200, -250)

def draw_line(num):
    cur_pos = doodle.position()
    for _ in range(num+1):
        doodle.dot(20, random.choice(rgb_colors))
        doodle.fd(50)
    doodle.setposition(cur_pos[0], cur_pos[1] + 50)


def draw_piece(num_lines, dots_per_line):
    for _ in range(num_lines):
        draw_line(dots_per_line)
    doodle.hideturtle()




draw_piece(10, 10)

screen.exitonclick()
