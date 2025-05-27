import pygame
from pygame.locals import *
import sys

def main():

    # sprite attributes

    x = 200
    y = 200
    w = 30
    h = 30
    velocity = 10

    # window size
    ww = 1000
    wh = 1000

    # initialize screen
    pygame.init()
    screen = pygame.display.set_mode((ww,wh))
    pygame.display.set_caption('Basic Pygame program')

    # load background image
    background = pygame.image.load('sprites/background-day.png').convert()
    background = pygame.transform.scale(background, (ww,wh))


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
        
        screen.blit(background, (0,0))

        pygame.draw.rect(screen, (255,0,0), (x,y,w,h))
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__': main()