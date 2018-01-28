import pygame
import random
import math
import mathematicals

GRAVITY = [0, 0.5]
WIND = [1, 0]
BLAST_RADIUS = 20
SCREEN_WIDTH = 1340
SCREEN_HEIGHT = 600
BALL_SIZE = 50


class Ball():
    def __init__(self):
        self.location = [720, 450]
        self.colour = self.get_colour()
        self.velocity = [random.randint(-BLAST_RADIUS, BLAST_RADIUS), random.randint(-BLAST_RADIUS, BLAST_RADIUS)]

    def get_colour(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return pygame.Color (red, green, blue)

    def move(self):
        self.location[0] = self.location[0] + self.velocity[0]
        self.location[1] = self.location[1] + self.velocity[1]

    def apply_forces(self):
        self.velocity = mathematicals.add_vectors(GRAVITY, self.velocity)
        if (self.location[1] <= 200):
            self.velocity = mathematicals.add_vectors(WIND, self.velocity)
        self.move()



    def check_collisions(self):
        distance_to_floor = (SCREEN_HEIGHT - BALL_SIZE / 2) - self.location[1]
        if (self.velocity[1] > distance_to_floor):
            # After this frame, we want the velocity to be exactly reversed
            self.velocity[1] = - self.velocity[1]
            # apply_forces() will remove this again later in the frame
            self.velocity[1] -= GRAVITY[1]

        if (self.location[0] >= (SCREEN_WIDTH - BALL_SIZE / 2) or (self.location[0] <= 0)):
            self.velocity[0] = - self.velocity[0]
        #subtract/add half ballsize from collision to ensure ball stays on screen



myimage = pygame.image.load("Booloon.png")
imagerect = myimage.get_rect()

def initialise():
    pygame.init()
    size=(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen=pygame.display.set_mode(size)
    pygame.font.init()
    myimage.convert_alpha()

    return screen


def render(screen, balls):

    screen.fill((226,226,226))
    for ball in balls:
        x = ball.location[0]
        y = ball.location[1]
        colour = ball.colour
        pygame.draw.ellipse(screen, colour, [x, y, BALL_SIZE, BALL_SIZE], 0)
    #screen.blit(myimage, (x, y))
    pygame.display.flip()


def run_game():
    screen = initialise()
    clock = pygame.time.Clock()
    carry_on = True
    balls = []
    for i in range(50):
        ball = Ball()
        balls.append(ball)


    while carry_on:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                carry_on = False
                print("bye bye")
                break
        for ball in balls:
            ball.check_collisions()
            ball.apply_forces()
        render(screen, balls)
        clock.tick(60)

run_game()
