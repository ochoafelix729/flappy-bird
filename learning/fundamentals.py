import pygame
from pygame.locals import *
import os

def main():

    x = 200
    y = 200
    w = 30
    h = 30
    velocity = 10

    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('Basic Pygame program')

    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    # event loop - necessary to keep window open
    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= velocity

        if keys[pygame.K_RIGHT]:
            x += velocity

        if keys[pygame.K_UP]:
            y -= velocity

        if keys[pygame.K_DOWN]:
            y += velocity
        
        screen.fill((0,0,0))

        pygame.draw.rect(screen, (255,0,0), (x,y,w,h))
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__': main()