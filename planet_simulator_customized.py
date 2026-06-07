# An orbit simulator of Trappist-1 Star System

# Trappist-1 planetary data sourced from:
# NASA Exoplanet Archive:
# https://exoplanetarchive.ipac.caltech.edu/overview/trappist-1

import pygame
import math
pygame.init() 

WIDTH, HEIGHT = 1500, 800 # Adjusted pygame window dimensions
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

FONT = pygame.font.SysFont('timesnewroman', 16)

class Planet:

    AU = 149.6e6 * 1000 # astronomical units in meters
    G = 6.67428e-11 
    scale = 10000 / AU # 1 AU = 10000 pixels, because star system is so compact, the scale is larger
    timestep = 3600 # changed timestep to 1 hour per frame since orbit is extremely fast

    def __init__(self, x, y, radius, color, mass):
        self.x = x 
        self.y = y 
        self.radius = radius # in km
        self.color = color 
        self.mass = mass # in kg

        self.x_vel = 0 
        self.y_vel = 0 

        self.star = False 
        self.dist_to_star = 0 
        self.orbit = [] 


    def draw(self, win): 
        x = self.x * self.scale + WIDTH / 2 
        y = self.y * self.scale + HEIGHT / 2 

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit: 
                x, y = point
                x = x * self.scale + WIDTH / 2
                y = y * self.scale + HEIGHT / 2
                updated_points.append((x,y))
            pygame.draw.lines(win, self.color, False, updated_points, 2) 

        pygame.draw.circle(win, self.color, (x, y), self.radius) 

        if not self.star: 
            distance_text = FONT.render(f"{round(self.dist_to_star/1000, 1)}km", 1, (255,255,255)) 
            win.blit(distance_text, (x - distance_text.get_width()/2,y - distance_text.get_height()/2))


    def attraction(self, other):
        other_x, other_y = other.x, other.y 
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)  

        if other.star:
            self.dist_to_star = distance
        
        force = self.G * self.mass * other.mass / distance **2
        theta = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        
        for planet in planets:
            if self.star: # make Trappist-1 fixed in place instead of moving realistically
                total_fx = total_fy = 0

            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.timestep 
        self.y_vel += total_fy / self.mass * self.timestep

        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x, self.y))

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

    # get orbital velocity using v = (2 * pi * r) / T
    # r = orbital radius in km, T = orbital period in seconds

    trappist_1b.y_vel = 83.365 * 1000
    trappist_1c.y_vel = 71.813 * 1000
    trappist_1d.y_vel = 60.732 * 1000
    trappist_1e.y_vel = 52.306 * 1000
    trappist_1f.y_vel = 45.637 * 1000
    trappist_1g.y_vel = 41.196 * 1000
    trappist_1h.y_vel = 35.910 * 1000

    planets = [star,trappist_1b, trappist_1c, trappist_1d, trappist_1e, trappist_1f, trappist_1g, trappist_1h]

    while running:
        clock.tick(60) 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False 

        WIN.fill('black')
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()
main()

