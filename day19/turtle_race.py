from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500 , height = 400)
user_guess = screen.textinput(title = "Make Your Bet." , prompt = "Guess the color of the turtle: ")

colors = ["red", "orange","yellow","green", "blue" ,"purple"]
y_positions = [-70,-40,-10,20,50,80]

if user_guess:
    is_race_on = True

all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtle.append(new_turtle)

while is_race_on:

    for turtle in all_turtle:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won !  the {winning_color} is the winner.")
            else:
                print(f"You have lost! the {winning_color} is the winner. ")

screen.exitonclick()