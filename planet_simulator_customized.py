# An orbit simulator of Trappist-1 Star System

# TRAPPIST-1 planetary data sourced from:
# NASA Exoplanet Archive:
# https://exoplanetarchive.ipac.caltech.edu/overview/trappist-1

import pygame
import math
pygame.init() 

WIDTH, HEIGHT = 1200, 800 # Adjusted pygame window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('TRAPPIST-1 Orbit Simulator')

star_color = (158, 33, 0)
trappistBColor = (86, 150, 156)
trappistCColor = (211, 189, 158)
trappistDColor = (50, 66, 95)
trappistEColor = (69, 82, 108)
trappistFColor = (234, 211, 193)
trappistGColor = (254, 241, 225)
trappistHColor = (227, 192, 167)

class Planet:

    AU = 149.6e6 * 1000 # astronomical units in meters, distance from earth to sun
    G = 6.67428e-11 
    scale = 10000 / AU # 1 AU = 10000 pixels, because star system is so compact the scale is larger
    timestep = 3600 * 24 

    def __init__(self, x, y, radius, color, mass):
        self.x = x 
        self.y = y 
        self.radius = radius # in km
        self.color = color 
        self.mass = mass # in kg

        self.x_vel = 0 
        self.y_vel = 0 

        self.star = False # whether or not the object is a star
        self.dist_to_star = 0 # distance to star
        self.orbit = [] # coordinate points the planet has traveled


    def draw(self, win): 
        x = self.x * self.scale + WIDTH / 2 
        y = self.y * self.scale + HEIGHT / 2 
        pygame.draw.circle(win, self.color, (x, y), self.radius) # draw circle with given aspects

# initializing planets and star, Trappist-1


def main():
    running = True 
    clock = pygame.time.Clock()

    # Creating Trappist-1 + planets 
    # trappist-1b, trappist-1c, trappist-1d, trappist-1e, trappist-1f, trappist-1g

    star = Planet(0, 0, 30, star_color, 1.79e29)
    star.star = True

    trappist_1b = Planet(-1 * (Planet.AU * 0.01154), 0, 16, trappistBColor, 8.2058e24)
    trappist_1c = Planet(-1 * (Planet.AU * 0.0158), 0, 15, trappistCColor, 7.81164e24)
    trappist_1d = Planet(-1 * (Planet.AU * 0.02227), 0, 12, trappistDColor, 2.31721e24)
    trappist_1e = Planet(-1 * (Planet.AU * 0.02925), 0, 13, trappistEColor, 4.13276e24)
    trappist_1f = Planet(-1 * (Planet.AU * 0.03849), 0, 14, trappistFColor, 6.20512e24)
    trappist_1g = Planet(-1 * (Planet.AU * 0.04683), 0, 17, trappistGColor, 7.88928e24)
    trappist_1h = Planet(-1 * (Planet.AU * 0.06189), 0, 10, trappistHColor, 1.94694e24)

    planets = [star, trappist_1b, trappist_1c, trappist_1d, trappist_1e, trappist_1f, trappist_1g, trappist_1h]

    # while game is running
    while running:
        clock.tick(60) 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False 

        WIN.fill('black')
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()
main()

