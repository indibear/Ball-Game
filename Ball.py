import pygame
import random
import math
import mathematicals
import physics



BLAST_RADIUS = 40 #20
SCREEN_WIDTH = 1340 #1340
SCREEN_HEIGHT = 600
GRAVITY = [0, 1.3] #0.5
WIND = [0, 0] #1, 0
VISCOSITY = 0.001



class Ball():
    def __init__(self):
        self.location = [720, 450]
        self.colour = self.get_colour()
        self.velocity = [random.randint(-BLAST_RADIUS, BLAST_RADIUS), random.randint(-BLAST_RADIUS, BLAST_RADIUS)]
        self.size = random.randint (8 , 80)


    def get_colour(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return pygame.Color (red, green, blue)

    def move(self):
        distance_to_floor = (SCREEN_HEIGHT - self.size) - self.location[1]
        if (self.velocity[1] > distance_to_floor):
            self.location[1] = (SCREEN_HEIGHT - self.size) - (self.velocity[1] - distance_to_floor)
            self.velocity[1] = - self.velocity[1]
            #reverse velocity, calculate the px we need to be above gorund in next frame
        else:
            self.location[1] = self.location[1] + self.velocity[1]

        self.location[0] = self.location[0] + self.velocity[0]



    def apply_forces(self):
        self.velocity = mathematicals.add_vectors(GRAVITY, self.velocity)
        x_friction = physics.calc_friction(VISCOSITY, self.size / 2, self.velocity[0])
        y_friction = physics.calc_friction(VISCOSITY, self.size / 2, self.velocity[1])
        friction = [-x_friction, -y_friction]
        #print(x_friction, y_friction)
        self.velocity = mathematicals.add_vectors(friction, self.velocity)
        if (self.location[1] <= 200):
            self.velocity = mathematicals.add_vectors(WIND, self.velocity)
        self.move()


    def check_collisions(self):
        distance_to_floor = (SCREEN_HEIGHT - self.size / 2) - self.location[1]
        if (self.velocity[1] > distance_to_floor):
        # After this frame, we want the velocity to be exactly reversed
            self.velocity[1] = - self.velocity[1]
            # apply_forces() will remove this again later in the frame
            self.velocity[1] -= GRAVITY[1]

        if (self.location[0] >= (SCREEN_WIDTH - self.size / 2) or (self.location[0] <= 0)):
            self.velocity[0] = - self.velocity[0]
