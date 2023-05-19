from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: ')

all_turtles = []
all_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for i in range(7):
    turtle = Turtle(shape='turtle')
    turtle.color(all_colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=i*40-110)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"Your turtle won! Go {winning_color}!")
            else:
                print(f"You lost. 😒  The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
