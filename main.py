import random
import turtle
from turtle import Turtle, Screen


# import colorgram
#
# colors = colorgram.extract('img.png', 30)
#
# # print(colors)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)
turtle.colormode(255)
color_list = [(195, 150, 109), (249, 244, 247), (138, 90, 60), (59, 37, 23), (58, 99, 127), (113, 156, 189),
              (161, 146, 56), (70, 108, 86), (58, 39, 46), (179, 159, 176), (205, 100, 65), (140, 179, 155),
              (104, 82, 92), (34, 54, 70), (218, 203, 125), (37, 57, 48), (45, 85, 31), (119, 114, 161), (103, 48, 32),
              (74, 51, 85), (228, 177, 161), (45, 62, 88), (96, 150, 117), (154, 106, 121), (174, 202, 183),
              (80, 64, 39), (202, 184, 192)]


def random_color():
    x = random.randint(0, len(color_list) - 1)
    return color_list[x]


dot = Turtle()
dot.speed(0)
dot.hideturtle()
dot.pu()
dot.goto(-250, -250)
# print(dot.position())

for j in range(10):
    # print(dot.ycor() + 20)
    new_y = dot.ycor() + 50
    dot.sety(new_y)
    dot.setx(-250)
    for i in range(10):
        # make a dot(20px), move 50 spaces, repeat
        # dot.showturtle()
        dot.color(random_color())
        dot.begin_fill()
        dot.circle(10)
        dot.end_fill()
        dot.pu()
        dot.fd(50)


screen = Screen()
screen.exitonclick()


