import math
import random
import turtle


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drew_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


turtle.speed(0)

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
drew_circle(5, "red")

phi = 360 / 7
r = 50
start = 0
answer = ""

for i in range(start, 7):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    drew_circle(22, "white")

while answer != "N":
    answer = turtle.textinput("Играем в Русскую рулетку?", "Y/N")
    if answer == "Y":

        for i in range(start, random.randrange(7,28)):
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
            drew_circle(22, "brown")
            drew_circle(22, "white")

        gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
        drew_circle(22, "brown")

        start = i % 7
        if start == 0:
            gotoxy(-150,250)
            turtle.write("Game over!", font=("Keystroke", 32, "normal"))
    else:
        pass
