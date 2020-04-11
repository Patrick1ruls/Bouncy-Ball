import turtle

class Bullet:
    def __init__(self):
        self.bullet = turtle.Turtle() # Initialize the player's bullet
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
        self.BULLET_SPEED = 20
        self.bullet_state = "fire" # Initialize bullet state (enum)
        #self.bullet.hideturtle() # Hide the bullet initially

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

    def fire(self, player):
        if self.bullet_state == "ready":
            #os.system("afplay laser.wav&") # Mac exclusive sound playing feature
            bullet_state = "fire"
            # Get player location so bullet can shoot from there
            self.x = player.xcor()
            self.y = player.ycor() + 20
            bullet.setposition(self.x, self.y)
            bullet.showturtle()
