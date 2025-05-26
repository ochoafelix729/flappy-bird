import pygame
from pygame.locals import *

def main():

    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((150,50))
    pygame.display.set_caption('Basic Pygame program')

    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    # blit to screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    # event loop - necessary to keep window open
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0,0))
        pygame.display.flip()

if __name__ == '__main__': main()