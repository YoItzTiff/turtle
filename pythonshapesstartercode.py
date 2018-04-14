from turtle import *
import math


# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,500)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
q = "Y"
while q == "Y":
    q = input("Do you want to draw a shape? Y/N: ")
    clear()
    if q == "Y":
        pencolor("blue")
        fillcolor("blue")
        begin_fill()
        x = int(input("Enter number of sides: "))
        pendown()
        for i in range(0, x):
              right(360/x)
              forward(50)
        end_fill()
        penup()
          





# Close window on click.
exitonclick()
