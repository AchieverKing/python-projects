from turtle import Turtle, Screen
import random

# timmy = Turtle()
# screen = Screen()
#
#
# # def move_forward():
# #     timmy.forward(10)
# #
# #
# screen.listen()
# # screen.onkey(key="space", fun=move_forward)
#
#
# def move_forward():
#     timmy.forward(10)
#
#
# def move_backward():
#     timmy.backward(10)
#
#
# def clockwise():
#     new_heading = timmy.heading() + 10
#     timmy.setheading(new_heading)
#     timmy.forward(10)
#
#
# def counterclockwise():
#     new_heading = timmy.heading() - 10
#     timmy.setheading(new_heading)
#     timmy.forward(10)
#
#
# def clear_drawing():
#     timmy.clear()
#     timmy.reset()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=clockwise)
# screen.onkey(key="d", fun=counterclockwise)
# screen.onkey(key="c", fun=clear_drawing)
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race: Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []
space = -100
position = 0
for col in colors:
    tim = Turtle(shape="turtle")
    tim.color(colors[position])
    position += 1
    tim.penup()
    tim.goto(x=-230, y=space)
    space += 40
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in all_turtles:
        if tim.xcor() > 230:
            is_race_on = False
            winning_color = tim.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color}  Turtle is the winner")
            else:
                print(f"You lose! The {winning_color} Turtle is the winner")
        else:
            pace_forward = random.randint(0, 10)
            tim.forward(pace_forward)

screen.exitonclick()
