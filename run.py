import pygame
from pygame import *

class Bird():
    def __init__(self, x, y):
        self.image = pygame.image.load('sprites/blue-bird-upflap')
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y


class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h

        self.bird = Bird(300,500)

        # create window
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        pygame.display.set_caption('Flappy Bird')

        # load background image
        self.background = pygame.image.load('sprites/background-day.png').convert()
        self.background = pygame.transform.scale(self.background, (self.window_w, self.window_h))

        # event loop
        run = True
        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # blit all visible elements
            self.window.blit(self.bird.image, (self.bird.x, self.bird.y))
            self.window.blit(self.background, (0,0))
            pygame.display.update()

game = Game(1000,1000)
