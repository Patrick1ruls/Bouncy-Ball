import turtle

wn = turtle.Screen()
wn.title("Stoplights with Classes")
wn.bgcolor("black")

stoplights = []

for _ in range(3):
    stoplights.append(turtle.Turtle()) # Create the turtle (initialization?)



class Stoplight():
    def __init__(self, x, y): # Initialize class
        # Draw boarder
        def draw_boarder():
            self.pen = turtle.Turtle() # Literally a pen for drawing a line
            self.pen.penup()
            self.pen.hideturtle()
            self.pen.speed(0)
            self.pen.color("purple")
            self.pen.goto(x - 30, y + 60)
            self.pen.width(3)
            self.pen.pendown()
            self.pen.fd(60)
            self.pen.rt(90)
            self.pen.fd(120)
            self.pen.rt(90)
            self.pen.fd(60)
            self.pen.rt(90)
            self.pen.fd(120)
        # Set up lights
        def init_lights():
            # Draw red light
            self.red_light = turtle.Turtle()
            self.red_light.shape("circle")
            self.red_light.color("grey")
            self.red_light.penup()
            self.red_light.speed(0)
            self.red_light.goto(x, y + 40)

            # Draw yellow light
            self.yellow_light = turtle.Turtle()
            self.yellow_light.shape("circle")
            self.yellow_light.color("grey")
            self.yellow_light.penup()
            self.yellow_light.speed(0)
            self.yellow_light.goto(x, y)

            # Draw green light
            self.green_light = turtle.Turtle()
            self.green_light.shape("circle")
            self.green_light.color("grey")
            self.green_light.penup()
            self.green_light.speed(0)
            self.green_light.goto(x, y - 40)

        draw_boarder()
        init_lights()

        self.color = "" # Track color

    def change_color(self, color):
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")

        if color == "red":
            self.red_light.color("red")
            self.color = "red"
        elif color == "yellow":
            self.yellow_light.color("yellow")
            self.color = "yellow"
        elif color == "green":
            self.green_light.color("green")
            self.color = "green"
        else:
            print("Error: Unknown Color {}".format(color))

    def timer(self):
        if self.color == "green":
            self.change_color("yellow")
            wn.ontimer(self.timer, 2000)
        elif self.color == "yellow":
            self.change_color("red")
            wn.ontimer(self.timer, 2000)
        elif self.color == "red":
            self.change_color("green")
            wn.ontimer(self.timer, 2000)

# Main Program
def main():
    # Create class instance
    stoplight1 = Stoplight(-90, 60)
    stoplight2 = Stoplight(0, 60)
    stoplight3 = Stoplight(90, 60)

    stoplight1.change_color("red")
    stoplight1.timer()
    stoplight2.change_color("yellow")
    stoplight2.timer()
    stoplight3.change_color("green")
    stoplight3.timer()


# Run Main
main()


turtle.mainloop()
