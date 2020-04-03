# Space Invaders Game with Classes
import turtle
import os
from Player import Player

# Initialize global variables
# Set up the screen
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders with Classes :D")

player1 = Player(0, -250, "blue", "triangle")
player1.show()






delay = raw_input("Press enter to finish.")
