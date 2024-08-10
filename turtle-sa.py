# Turtle Party Project
# by Ray Brown
import turtle

turtle.shape("turtle")

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)
def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def house(len):
    square(len)
    triangle(len)

def main():
    turtle.speed(0)
    turtle.color("green")
    house(100)
    turtle.color("blue")
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    house(50)


main()
turtle.Screen().exitonclick()
