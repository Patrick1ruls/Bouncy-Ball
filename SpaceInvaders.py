# Space Invaders
# Set up the screen
import turtle
import os

# Global variables
X_POS = -300
Y_POS = -300
BORDER_SIZE = 600

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

def draw_border(x, y, size):
    # Draw boarder
    border_pen = turtle.Turtle() # Initialize object
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(x, y) # Bottom left
    border_pen.pensize(3)
    border_pen.pendown()
    for side in range(4):
        border_pen.fd(size)
        border_pen.lt(90) # Left turn
    border_pen.hideturtle()

def main():
    draw_border(X_POS, Y_POS, BORDER_SIZE)









# Main program
main()

delay = raw_input("Press enter to finish.")
#turtle.mainloop()
