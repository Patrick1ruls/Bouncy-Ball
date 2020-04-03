import turtle

class Bullet:
    def __init__(self, x, y):
        self.bullet = turtle.Turtle() # Initialize the player's bullet
        self.x = x
        self.y = y
        self.BULLET_SPEED = 20
        self.bullet_state = "ready" # Initialize bullet state (enum)
        self.color = "yellow"
        self.shape = "triangle"
        self.bullet.color(self.color)
        self.bullet.shape(self.shape)
        self.bullet.penup()
        self.bullet.speed(0)
        self.bullet.setheading(90)
        self.bullet.shapesize(0.5, 0.5)
        #self.bullet.hideturtle() # Hide the bullet initially
        self.BULLET_SPEED = 20
        self.bullet_state = "ready" # Initialize bullet state (enum)
        self.move() # Set the bullets movement

    def move(self):
        # Define bullet states | ready - ready to fire | fire - bullet is firing
        if self.bullet_state == "fire":
            self.y = self.bullet.ycor()
            self.y += self.BULLET_SPEED
            self.bullet.sety(self.y)
        # Border check
        if self.bullet.ycor() > 275:
            self.bullet.hideturtle()
            self.bullet_state = "ready"
