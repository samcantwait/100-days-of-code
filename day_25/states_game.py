import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.tolist()
entered_states = []

while len(entered_states) < 50:
    answer_state = screen.textinput(title=f"{len(entered_states)}/50 States Correct", prompt="What is another state's name? ").title()
    if answer_state == 'Exit':
        remaining_states = []
        for state in all_states:
            if state not in entered_states:
                remaining_states.append(state)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.values and answer_state not in entered_states:
        [state, x, y] = data[data['state'] == answer_state].values.flatten().tolist()
        entered_states.append(state)
        s = turtle.Turtle()
        s.penup()
        s.hideturtle()
        s.goto(x, y)
        s.write(state)