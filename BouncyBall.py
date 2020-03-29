## Practice Coding by making a call that bounces around the window
import turtle
import random

## Set globals
WIDTH, HEIGHT = 600, 400 ## Set screen dimensions
SIZE = 2 ## Seems to be mult by 10ish
SPEED = 10
## Screen boundaries
NBOUND = (HEIGHT / 2) - SIZE * 10
EBOUND = WIDTH / 2 - SIZE * 15
SBOUND = -(HEIGHT / 2 - 10) + SIZE * 10
WBOUND = -WIDTH / 2 + SIZE * 11


## Create window
wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.bgcolor("purple")
wn.title("Bouncing Ball Simulator")
wn.tracer(0) # Stops the screen from updating

## Create ball
ball = turtle.Turtle()
ball.shape("circle") ## All objects start in center of window
ball.shapesize(SIZE) ## Set the balls size
ball.color("green")
ball.penup()
ball.dy = random.randrange(-SPEED, SPEED) ## Setting a variable for delta y (will control y movement, - is down)
ball.dx = random.randrange(-SPEED, SPEED)

while True:
    wn.update()
    ball.sety(ball.ycor() + ball.dy) ## Make the ball move!!
    ball.setx(ball.xcor() + ball.dx) ## Make the ball move!!

    ## Check for screen boundary
    if (ball.ycor() < SBOUND) or (ball.ycor() > NBOUND):
        ball.dy *= -1 ## Set bouncy in opposite direction
    if (ball.xcor() < WBOUND) or (ball.xcor() > EBOUND):
        ball.dx *= -1 ## Set bouncy in opposite direction

turtle.mainloop() ## Ensures program runs
