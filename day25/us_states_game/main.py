import turtle
import os
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")


image_file = os.path.join(os.path.dirname(__file__) , "blank_states_img.gif")
screen.addshape(image_file)
turtle.shape(image_file)

game_is_on = True
file_name = os.path.join(os.path.dirname(__file__) , "50_states.csv")
data = pd.read_csv(file_name)

all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 correct" , 
                                         prompt= " what's the another state name?").title()
    # print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(os.path.join(os.path.dirname(__file__) , "missing_sate.csv"))
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]) , int(state_data["y"]))
        t.write(answer_state)

screen.exitonclick()