import turtle
from turtle import Turtle,Screen
from random import choice
from bobfunctions import draw_dots
from color_lists import color_list

turtle.colormode(255)



bob = Turtle(shape="circle",visible=False)
bob.pensize(10)
bob.penup()
bob.setposition(-250,-250)
bob.pendown()


pos_y = -200
for i in range (10):
    draw_dots(bob)

    bob.hideturtle()
    bob.penup()
    bob.setposition(-250,pos_y)
    pos_y += 50
    bob.showturtle()
    bob.pendown()

    bob.color(choice(color_list))

bob.hideturtle()




screen = Screen()
screen.exitonclick()
