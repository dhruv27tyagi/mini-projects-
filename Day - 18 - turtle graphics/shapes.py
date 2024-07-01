from turtle import Turtle,Screen

tim=  Turtle()


def draw_shape(sides):
        angle = 360/sides
        for _ in range(sides):
            tim.forward(100)
            tim.right(angle)
    
for i in range(3,11):    
    draw_shape(i)


screen = Screen()
screen.exitonclick()