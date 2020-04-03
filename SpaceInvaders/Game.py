# Space Invaders Game with Classes
import turtle
import os
from Player import Player

class Game:
    def __init__(self):
        # Initialize global variables
        # Set up the screen
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Space Invaders with Classes :D")

    # Initialize game
    def init(self):
        player1 = Player(0, -250, "blue", "triangle")
        player1.show()





game = Game()
game.init()
delay = raw_input("Press enter to finish.")
