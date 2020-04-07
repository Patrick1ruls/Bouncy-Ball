# Space Invaders
# Set up the screen
import turtle
import os
import math
import random

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
bullet = turtle.Turtle() # Initialize the player's bullet
BULLET_SPEED = 20
bullet_state = "ready" # Initialize bullet state (enum)
score = 0 # Initialize score
score_pen = turtle.Turtle()

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
    for enemy in enemies:
        # Check for a collision with bullet and enemy
        if isCollision(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            global score
            score += 10
            update_score(score_pen, score)


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

def create_enemy():
    global ENEMY_SPEED
    ENEMY_SPEED = 2
    global number_of_enemies
    number_of_enemies = 5
    global enemy # Initialize enemy and make global
    #enemy = turtle.Turtle()
    global enemies
    enemies = [] # Create empty list of numbers
    # Add enemies to list
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())
    # Set enemy attributes
    for enemy in enemies:
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

def move_enemy():
    global ENEMY_SPEED
    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += ENEMY_SPEED
        enemy.setx(x)
        # Move ALL enemies back and down
        if enemy.xcor() > 280:
            # Nested loop
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            ENEMY_SPEED *= -1 # Only need to change once
        # Move ALL enemies back and down
        if enemy.xcor() < -280:
            # Nested loop
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            ENEMY_SPEED *= -1 # Only need to change once

# Bullet enemy collision checking
def isCollision(turtle1, turtle2):
    # Pythagorean therom a^2 + b^2 = c^2
    distance = math.sqrt(math.pow(turtle1.xcor()-turtle2.xcor(), 2) + math.pow(turtle1.ycor()-turtle2.ycor(), 2))
    if distance < 15:
        return True

# Handle scoring
def init_score(turtle):
    # Draw the score
    turtle.speed(0)
    turtle.color("white")
    turtle.penup()
    turtle.setposition(-290,280)
    score_string = "Score: %s" %score
    turtle.write(score_string, False, align = "left", font = ("Arial", 14, "normal"))
    turtle.hideturtle()

def update_score(turtle, score):
    score_string = "Score: %s" %score
    turtle.write(score_string, False, align = "left", font = ("Arial", 14, "normal"))


# Initialize program
def init():
    draw_border(X_POS, Y_POS, BORDER_SIZE)
    create_player(x_start, y_start)
    create_bullet()
    set_movement()
    create_enemy()
    init_score(score_pen)



# Main game loop
init()
while True:
    move_enemy()
    move_bullet()



    for enemy in enemies:
        # Check for a collision with player and enemy (enemy)
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break # Exit game loop (Oh that's so easy and simple!)




delay = raw_input("Press enter to finish.")
