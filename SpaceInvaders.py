# Space Invaders
# Set up the screen
import turtle
import os

# Global variables
X_POS = -300
Y_POS = -300
BORDER_SIZE = 600
player = turtle.Turtle() # Initialize player and make global
x_start = 0
y_start = -250
PLAYER_SPEED = 15 # How fast the player will move
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

def create_player(x, y):
    # Create player turtle
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(x, y)
    player.setheading(90)

# Let player left and right
def move_left():
    x = player.xcor()
    x -= PLAYER_SPEED
    # Boundary check
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += PLAYER_SPEED
    # Boundary check
    if x > 280:
        x = 280
    player.setx(x)

# Create keyboard bindings
def set_movement():
    turtle.listen()
    turtle.onkey(move_left, "Left") # When pressing left arrow, uses move_left function
    turtle.onkey(move_right, "Right") # When pressing left arrow, uses move_left function

def main():
    draw_border(X_POS, Y_POS, BORDER_SIZE)
    create_player(x_start, y_start)
    set_movement()









# Main program
main()

delay = raw_input("Press enter to finish.")
#turtle.mainloop()
