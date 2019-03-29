import math
import random
import turtle
import myrobot

phi = 360 / 7
r = 50


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drew_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def drew_baraban(base_x, base_y):
    gotoxy(base_x, base_y)
    turtle.circle(80)
    gotoxy(base_x, base_y + 160)
    drew_circle(5, "red")

    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r +
               60)
        drew_circle(22, "white")


def turn_baraban(base_x, base_y, start):
    for i in range(start, random.randrange(7, 28)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r +
               60)
        drew_circle(22, "brown")
        drew_circle(22, "white")

    gotoxy(base_x +math.sin(phi_rad) * r, base_y + math.cos(phi_rad) * r + 60)
    drew_circle(22, "brown")

    return i % 7


turtle.speed(0)

drew_baraban(0, 0)

start = 0
answer = ""

while answer != "n":
    answer = turtle.textinput("Играем в Русскую рулетку?", "y/n")
    if answer == "y":
        start = turn_baraban(0, 0, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Game over!", font=("Keystroke", 32, "normal"))
            myrobot.duble_files(".")

    else:
        pass
