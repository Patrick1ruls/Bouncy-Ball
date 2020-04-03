# Space Invaders
# Set up the screen
import turtle
import os
import math


# Global variables
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
X_POS = -300
Y_POS = -300
BORDER_SIZE = 600
player = turtle.Turtle() # Initialize player and make global
x_start = 0
y_start = -250
PLAYER_SPEED = 15 # How fast the player will move
enemy = turtle.Turtle() # Initialize enemy and make global
ENEMY_SPEED = 2
bullet = turtle.Turtle() # Initialize the player's bullet
BULLET_SPEED = 20
bullet_state = "ready" # Initialize bullet state (enum)

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

def create_bullet():
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle() # Hide the bullet initially

def fire_bullet():
    # Declare bullet state as a global if it needs to change
    global bullet_state # global means the function can change this variable
    if bullet_state == "ready":
        bullet_state = "fire"
        # Get player location so bullet can shoot from there
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x, y)
        bullet.showturtle()

def move_bullet():
    # Define bullet states | ready - ready to fire | fire - bullet is firing
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += BULLET_SPEED
        bullet.sety(y)
    # Border check
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"
    # Check for a collision with bullet and enemy
    if isCollision(bullet, enemy):
        # Reset bullet
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        # Reset enemy
        enemy.setposition(-200, 250)

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
    turtle.onkey(fire_bullet, "space")

def create_enemy(x, y):
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(x, y)

def move_enemy():
    # Move enemy
    global ENEMY_SPEED
    x = enemy.xcor()
    x += ENEMY_SPEED
    enemy.setx(x)
    # Move enemy back and down
    if enemy.xcor() > 280:
        ENEMY_SPEED *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
    if enemy.xcor() < -280:
        ENEMY_SPEED *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

# Bullet enemy collision checking
def isCollision(turtle1, turtle2):
    # Pythagorean therom a^2 + b^2 = c^2
    distance = math.sqrt(math.pow(turtle1.xcor()-turtle2.xcor(), 2) + math.pow(turtle1.ycor()-turtle2.ycor(), 2))
    if distance < 15:
        return True

# Initialize program
def init():
    draw_border(X_POS, Y_POS, BORDER_SIZE)
    create_player(x_start, y_start)
    create_bullet()
    set_movement()
    create_enemy(-200, 250)



init()
# Main game loop
while True:
    move_enemy()
    move_bullet()




delay = raw_input("Press enter to finish.")
