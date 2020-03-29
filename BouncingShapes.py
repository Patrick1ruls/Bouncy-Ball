## Practice Coding by making a call that bounces around the window
import turtle
import random

## Create window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0) # Stops the screen from updating

balls = [] # Make multiple balls

for _ in range(25):
    balls.append(turtle.Turtle()) # Create the turtle (initialization?)

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ## Create each ball
    ball.shape(random.choice(shapes)) ## All objects start in center of window
    ball.color(random.choice(colors))
    ball.penup() ## Removes annoying line that follows ball
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y) ## Sends ball to that location
    ball.dy = 0 ## Setting a variable for delta y (will control y movement, - is down)
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5) # delta angle (for rotation)

gravity = 0.1 # Force that will pull ball downwards

while True:
    wn.update() # Provides performance improvement with tracer(0)

    for ball in balls:
        ball.dy -= gravity
        ball.rt(ball.da) # rt = rotate right
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        ## Check for screen boundaries
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
        if ball.xcor() > 300 or ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1





turtle.mainloop() ## Ensures program runs
