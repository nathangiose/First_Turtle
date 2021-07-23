from turtle import *

color('Green')
bgcolor('Black')
speed(10)
hideturtle()

b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1