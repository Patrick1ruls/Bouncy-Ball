import turtle
import os



class Player:
    def __init__(self, x, y, color, shape):
        self.player = turtle.Turtle() # Initialize player and make global
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.PLAYER_SPEED = 15

    def show(self):
        # Create player turtle
        self.player.color(self.color)
        self.player.shape(self.shape)
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(self.x, self.y)
        self.player.setheading(90)

    # Let player left and right
    def move_left(self):
        self.x = self.player.xcor()
        self.x -= self.PLAYER_SPEED
        # Boundary check
        if self.x < -280:
            self.x = -280
        self.player.setx(self.x)

    def move_right(self):
        self.x = self.player.xcor()
        self.x += self.PLAYER_SPEED
        # Boundary check
        if self.x > 280:
            self.x = 280
        self.player.setx(self.x)

    # Create keyboard bindings
    def set_movement(self):
        turtle.listen()
        turtle.onkey(self.move_left, "Left") # When pressing left arrow, uses move_left function
        turtle.onkey(self.move_right, "Right") # When pressing left arrow, uses move_left function
