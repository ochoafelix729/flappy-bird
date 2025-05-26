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

if __name__ == '__main__': main()