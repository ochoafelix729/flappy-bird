import pygame
from pygame import *
import sys

class Bird():
    def __init__(self, x, y):
        self.image = pygame.image.load('sprites/blue-bird-upflap')
        self.width = image.get_width()
        self.height = image.get_height()


class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h

        # create window
        pygame.init()
        window = pygame.display.set_mode((self.window_w, self.window_h))
        pygame.display.set_caption('Flappy Bird')

        # load background image
        background = pygame.image.load('sprites/background-day.png').convert()
        background = pygame.transform.scale(window, (self.window_w, self.window_h))

        # event loop
        run = True
        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            window.blit(background, (0,0))

game = Game(1000,1000)
