import turtle as t 
import random

tim = t.Turtle()

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(100):
    tim.forward(50)
    tim.setheading(random.choice(directions))