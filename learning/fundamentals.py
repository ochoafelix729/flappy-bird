import pygame
from pygame.locals import *
import os

def main():

    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((150,50))
    pygame.display.set_caption('Basic Pygame program')

    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    # event loop - necessary to keep window open
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        pygame.draw.rect(screen, (255,0,0) (30,30,30,30))
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__': main()