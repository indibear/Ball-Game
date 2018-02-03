import pygame
import random
import math
import mathematicals
import physics
from Ball import Ball


GRAVITY = [0, 1.3] #0.5
WIND = [0, 0] #1, 0
SCREEN_WIDTH = 1340 #1340
SCREEN_HEIGHT = 600
NUMBER_OF_BALLS = 11


def initialise():
    pygame.init()
    size=(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen=pygame.display.set_mode(size)
    pygame.font.init()
    return screen


def render(screen, balls):
    screen.fill((226,226,226))
    for ball in balls:
        x = ball.location[0]
        y = ball.location[1]
        colour = ball.colour
        pygame.draw.ellipse(screen, colour, [x, y, ball.size, ball.size], 0)
    #screen.blit(myimage, (x, y))
    pygame.display.flip()


def run_game():
    screen = initialise()
    clock = pygame.time.Clock()
    carry_on = True
    balls = []
    for i in range(NUMBER_OF_BALLS):
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
