import pygame
import math
pygame.init() # initialize pygame modules

# Set up pygame window
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # size of window
pygame.display.set_caption('Planet Orbit Simulator')

# set Planet class
class Planet:

    # constants
    AU = 149.6e6 * 1000 # astronomical units in meters, distance from earth to sun
    G = 6.67428e-11# gravitional constant
    scale = 250 / AU # what a meter represents on the scale of pygame window. 
                     # 1 AU = 100 pixels
    timestep = 3600 * 24 # how much time passes at a time

    def __init__(self, x, y, radius, color, mass):
        self.x = x # x position of planet
        self.y = y # y position of planet
        self.radius = radius # radius of planet
        self.color = color # color of planet
        self.mass = mass # mass of planet, in kg

        self.x_vel = 0 # horizontal velocity in which planet is moving
        self.y_vel = 0 # vertical velocity in which planet is moving

        self.sun = False # whether or not the object is a sun
        self.dist_to_sun = 0 # distance to sun
        self.orbit = [] # points the planet has traveled


    def draw(self, win): # draws planet on screen
        x = self.x * self.scale + WIDTH / 2 # set x position to scale and in center
        y = self.y * self.scale + HEIGHT / 2 # set y position to scale and in center
        pygame.draw.circle(win, self.color, (x, y), self.radius) # draw circle with given aspects

# initializing planets and sun


def main():
    running = True # Set pygame event to keep game running
    clock = pygame.time.Clock() # set frame rate

    # Creating the sun + planets
    sun_color = (255, 255, 0)
    sun = Planet(0, 0, 30, sun_color, 1.98892e30)
    sun.sun = True

    #earth =

    planets = [sun]


    # while game is running
    while running:
        clock.tick(60) # Frame rate up to 60 fps

        for event in pygame.event.get(): # Different events
            if event.type == pygame.QUIT: # Handling the event where user exits out game
                running = False # Closes window

        WIN.fill('black')
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update() # display every update

    pygame.quit()
main()

