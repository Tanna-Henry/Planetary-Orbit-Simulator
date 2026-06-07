import pygame
import math
pygame.init() # initialize pygame modules

# Set up pygame window
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # size of window
pygame.display.set_caption('Planet Orbit Simulator')

sun_color = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GRAY = (80, 78, 81)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont('timesnewroman', 16)


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

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit: # all x, y coordinates to scale
                x, y = point
                x = x * self.scale + WIDTH / 2
                y = y * self.scale + HEIGHT / 2
                updated_points.append((x,y))
            pygame.draw.lines(win, self.color, False, updated_points, 2) # takes list of points, draws lines between them

        
        pygame.draw.circle(win, self.color, (x, y), self.radius) # draw circle with given aspects

        if not self.sun: # if object is not the sun
            distance_text = FONT.render(f"{round(self.dist_to_sun/1000, 1)}km", 1, WHITE) # write distance to sun for each planet
            win.blit(distance_text, (x - distance_text.get_width()/2,y - distance_text.get_height()/2)) # shifts text to the middle



    def attraction(self, other):
        other_x, other_y = other.x, other.y # gets coordinates
        distance_x = other_x - self.x # distance between current planet and second object
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2) # distance formula 

        if other.sun:
            self.dist_to_sun = distance
        
        # calculate force of attraction
        force = self.G * self.mass * other.mass / distance **2
        theta = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.timestep # F = ma :: a = f / m
        self.y_vel += total_fy / self.mass * self.timestep

        # update positions, then draw
        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x,self.y))

# initializing planets and sun


def main():
    running = True # Set pygame event to keep game running
    clock = pygame.time.Clock() # set frame rate

    # Creating the sun + planets
    sun = Planet(0, 0, 30, sun_color, 1.98892e30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16 , BLUE, 5.9742e24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39e23)
    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GRAY, 3.30e23)
    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685e24)

    # exisiting vertical velocity
    earth.y_vel = 29.783 * 1000
    mars.y_vel = 24.077 * 1000
    mercury.y_vel = 47.4 * 1000
    venus.y_vel = 35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]


    # while game is running
    while running:
        clock.tick(60) # Frame rate up to 60 fps

        for event in pygame.event.get(): # Different events
            if event.type == pygame.QUIT: # Handling the event where user exits out game
                running = False # Closes window

        WIN.fill('black')
        for planet in planets:
            planet.update_position(planets) # update positions of planets
            planet.draw(WIN)

        pygame.display.update() # display every update

    pygame.quit()
main()

