import turtle
import os



class Player:
    def __init__(self, x, y, color, shape):
        self.player = turtle.Turtle() # Initialize player and make global
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape

    def show(self):
        # Create player turtle
        self.player.color(self.color)
        self.player.shape(self.shape)
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(self.x, self.y)
        self.player.setheading(90)
