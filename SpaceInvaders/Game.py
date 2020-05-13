# Space Invaders Game with Classes
import turtle
import os
from Player import Player
from Bullet import Bullet

# Global variables
X_POS = -300
Y_POS = -300
BORDER_SIZE = 600
x_start = 0
y_start = -250
player_color = "blue"
player_shape = "triangle"

class Game:
    def __init__(self, x, y, size):
        # Initialize global variables
        # Set up the screen
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Space Invaders with Classes :D")
        # Draw boarder
        self.border_pen = turtle.Turtle() # Initialize object
        self.border_pen.speed(0)
        self.border_pen.color("white")
        self.border_pen.penup()
        self.border_pen.setposition(x, y) # Bottom left
        self.border_pen.pensize(3)
        self.border_pen.pendown()
        for side in range(4):
            self.border_pen.fd(size)
            self.border_pen.lt(90) # Left turn
        self.border_pen.hideturtle()

    # Initialize game
    def init(self):
        self.player = Player(x_start, y_start, player_color, player_shape) # Create the player
        self.bullet = Bullet()
        self.set_movement()

    # Create keyboard bindings
    def set_movement(self):
        turtle.listen()
        turtle.onkey(self.player.move_left, "Left") # When pressing left arrow, uses move_left function
        turtle.onkey(self.player.move_right, "Right") # When pressing left arrow, uses move_left function
        turtle.onkey(self.bullet.fire, "space")

    # Main game loop
    def play(self):
        self.init()
        while True:
            self.bullet.move()


game = Game(X_POS, Y_POS, BORDER_SIZE)
game.play()


delay = raw_input("Press enter to finish.")
