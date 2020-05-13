# Pygame template/skeleton
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30
# Define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (125, 0, 125)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init() # Sound  effects
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure Game Tutorial")
clock = pygame.time.Clock()

# Game loop
running = True # Variable for stoping game loop
while running:
    clock.tick(FPS) # Keep game running at right speed
    """ Process input(events) """
    for event in pygame.event.get(): # Gather all events during loop
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

    """ Update """


    """ Draw/render """
    screen.fill(BLACK)
    # Do this after drawing everything
    pygame.display.flip() # Fancy "double buffering"

pygame.quit()

"""
pygame.init() # Always do at start of pygame programs
# Set up the program window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adventure Game Tutorial") # Window title

x = 50
y = 50
width = 40
height = 60
vel = 5

# Main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get(): # Reads in all events to the program
        if event.type == pygame.QUIT: # Exit when clicking the red button
            run = False

    # Draw character
    pygame.draw.rect(win, (125, 0, 125), (x, y, width, height))
    pygame.display.update()

pygame.quit()
"""
