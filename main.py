import turtle
from turtle import Turtle, Screen
import random


new_turtle = Turtle()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
new_turtle.ht()


all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(-200, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


        rand_distance = random.randint(0, 10)
        turtle.forward((rand_distance))




# tom = Turtle(shape='turtle')
# tom.penup()
# tom.goto(-200, -60)
#
# tam = Turtle(shape='turtle')
# tam.penup()
# tam.goto(-200, -20)
#
# ten = Turtle(shape='turtle')
# ten.penup()
# ten.goto(-200, 20)
#
# tad = Turtle(shape='turtle')
# tad.penup()
# tad.goto(-200, 60)
#
# ted = Turtle(shape='turtle')
# ted.penup()
# ted.goto(-200, 100)


screen.exitonclick()