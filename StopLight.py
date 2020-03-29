import turtle
import time

def setup():
    wn = turtle.Screen()
    wn.title("Stoplights")
    wn.bgcolor("black")

# Draw box around the stoplight
def draw_box():
    pen = turtle.Turtle() # Literally a pen for drawing a line
    pen.color("yellow")
    pen.width(3)
    pen.hideturtle()
    pen.penup()
    pen.goto(-30, 60)
    pen.pendown()
    pen.fd(60)
    pen.rt(90)
    pen.fd(120)
    pen.rt(90)
    pen.fd(60)
    pen.rt(90)
    pen.fd(120)





def main():
    setup()
    draw_box()


    # Draw red light
    red_light = turtle.Turtle()
    red_light.shape("circle")
    red_light.color("grey")
    red_light.penup()
    red_light.goto(0, 40)

    # Draw yellow light
    yellow_light = turtle.Turtle()
    yellow_light.shape("circle")
    yellow_light.color("grey")
    yellow_light.penup()
    yellow_light.goto(0, 0)

    # Draw green light
    green_light = turtle.Turtle()
    green_light.shape("circle")
    green_light.color("grey")
    green_light.penup()
    green_light.goto(0, -40)

    # Change lights
    while True:
        red_light.color("red")
        time.sleep(2)
        red_light.color("grey")

        green_light.color("green")
        time.sleep(2)
        green_light.color("grey")

        yellow_light.color("yellow")
        time.sleep(2)
        yellow_light.color("grey")


main()







turtle.mainloop()
