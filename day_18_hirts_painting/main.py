# import colorgram
#
# dave = colorgram.extract("hirst.jpg", 300)
# # print(dave)
#
# color_list = []
# for colors in dave:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)
import turtle
import random
from turtle import Turtle, Screen
turtle.colormode(255)
new_color_list = [(207, 157, 109), (191, 147, 166),
                  (128, 168, 195), (230, 214, 96), (40, 108, 156), (118, 184, 144), (124, 76, 93), (43, 126, 75),
                  (52, 18, 30), (147, 78, 60), (225, 171, 195), (59, 168, 116), (43, 23, 15), (214, 90, 67),
                  (118, 36, 50), (170, 174, 49), (181, 96, 112), (14, 97, 56), (58, 159, 177), (157, 212, 181),
                  (24, 22, 35), (239, 169, 159), (181, 185, 214), (120, 37, 29), (87, 123, 186), (16, 42, 22),
                  (157, 206, 213), (216, 219, 19), (62, 49, 92), (8, 93, 105), (69, 65, 48)]

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(new_color_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


screen = Screen()
screen.exitonclick()
