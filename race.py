from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
x_position = -150
go = [5,10,15]
turtles = []

for turtle_index in range(0, 6):
    tim = Turtle()
    tim.color(colors[turtle_index])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x_position, y_positions[turtle_index])
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is a winner!")
            else:
                print(f"You've lost! The {winning_color} is not a winner!")

        turtle.forward(random.choice(go))



screen.exitonclick()