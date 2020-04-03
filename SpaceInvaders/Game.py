# Space Invaders Game with Classes
import turtle
import os
from Player import Player

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
        player1 = Player(x_start, y_start, player_color, "triangle") # Create the player
        player1.show() # Show player on screen
        player1.set_movement()


    # Main game loop
    def play(self):
        self.init()
        while True:
            print("Test")
            delay = raw_input("Press enter to finish.")


game = Game(X_POS, Y_POS, BORDER_SIZE)
game.play()


delay = raw_input("Press enter to finish.")
