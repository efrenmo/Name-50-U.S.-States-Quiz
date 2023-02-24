import turtle
from turtle import Turtle
import pandas as pd
screen = turtle.Screen()
prompt_window = turtle.Screen()


image = "./blank_states_img.gif"
screen.addshape(image)
screen.title("U.S. States Quiz Game")

map_turtle = Turtle()
map_turtle.shape(image)

# Turtle instance to write states' name on map
state_turtle = Turtle()
state_turtle.hideturtle()
state_turtle.penup()

FONT = ("Courier", 11, "bold")
ALIGNMENT= "center"

# Code needed to obtain the coordinates of each state using your mouse
# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor())

data = pd.read_csv("50_states.csv")
print(data)


states_list = data["state"].to_list()
print(states_list)

def state_in_list(answer):
    if answer in states_list:
        return True
def calc_missing_states():
    for state in states_list:
        if state not in correct_answers_list:
            missing_states.append(state)

def write_to_map(state):
    state_coordinates = data[data["state"] == state]
    state_x = int(state_coordinates["x"])
    state_y = int(state_coordinates["y"])
    state_turtle.goto(state_x, state_y)
    state_turtle.write(f"{state}", align=ALIGNMENT, font=FONT)

correct_answers_list = []
missing_states = []

while len(correct_answers_list) < 50:
    answer_state = prompt_window.textinput(title=f"{len(correct_answers_list)}/50 Guess the State",
                                           prompt="What is another state's name?"
                                           )
    # Convert answer to Title Case
    answer_state = answer_state.title()

    # States that were not recalled are saved to a csv file for review
    if answer_state == "Exit":
        for state in states_list:
            if state not in correct_answers_list:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Plots the remainder states that have not been input on the prompt window
    if answer_state == "Solution":
        calc_missing_states()
        print(missing_states)
        for state in missing_states:
            state_turtle.color("red")
            write_to_map(state)

    # Correct answers are plotted to the map
    if state_in_list(answer_state):
        if answer_state not in correct_answers_list:
            correct_answers_list.append(answer_state)
            state_turtle.color("black")
            write_to_map(answer_state)




