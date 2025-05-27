import pygame
from pygame import *
import sys

class Bird():
    def __init__(self, x, y):
        self.image = pygame.image.load('sprites/bluebird-upflap.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        self.falling = True
        self.jumpforce = 100

        self.bird_frames = [
            pygame.image.load('sprites/bluebird-upflap.png'),
            pygame.image.load('sprites/bluebird-midflap.png'),
            pygame.image.load('sprites/bluebird-downflap.png')
        ]

    def jump(self):
        self.y -= self.jumpforce


class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h
        self.gravity = 20

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
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.bird.jump()

            # gravity
            self.bird.y += self.gravity

            # blit all visible elements
            self.window.blit(self.background, (0,0))
            self.window.blit(self.bird.image, (self.bird.x, self.bird.y))
            pygame.display.update()


game = Game(1000,1000)
