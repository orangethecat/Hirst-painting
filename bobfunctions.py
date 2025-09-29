from random import choice

#YES. I HAVE MADE MY TURTLES NAME BOB.


def bob_color(bob):
    color_list = [(240, 246, 242), (239, 242, 247), (198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121),
                  (167, 153, 48), (132, 34, 23)]
    random_color = choice(color_list)
    for color in random_color:
        r = random_color[0]
        g = random_color[1]
        b = random_color[2]
        new_color = (r, g, b)
        bob.color(new_color)

def draw_dots(bob):
    for i in range(10):
        bob.stamp()
        bob.penup()
        bob.forward(50)
        bob.pendown()
        bob_color(bob)

    bob.stamp()


def set_bobs_position(bob):
    pos_y = -200
    bob.hideturtle()
    bob.penup()
    bob.setposition(-250, pos_y)
    pos_y += 50
    bob.showturtle()
    bob.pendown()
