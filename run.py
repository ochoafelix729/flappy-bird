import pygame
from pygame import *
import sys

class Sprite():
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()


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


    def jump(self):
        self.y -= self.jumpforce


class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h
        self.gravity = 20
        self.curr_screen = 'gameplay'
        

        

        # create window
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        pygame.display.set_caption('Flappy Bird')

        # for gameplay screen
        self.bird = Bird(300,500)

        # for gameover screen
        self.active = False
        self.button_rect = None
        self.font = pygame.font.SysFont(None, 24)
        self.button_color = (255,204,0)
        self.hover_color = (255,170,0)
        self.color = None

        
        # event loop
        self.run = True
        while self.run:
            pygame.time.delay(50)

            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_click = pygame.mouse.get_pressed()

            self.handleEvents()

            if self.curr_screen == 'gameplay':
                self.drawGamePlay()
                self.updateGamePlay()
            
            elif self.curr_screen == 'gameover':
                self.drawGameOver()
                self.updateGameOver()
       
            pygame.display.update()


    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
    

    def updateGamePlay(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bird.jump()

        if self.bird.y > (self.window_h - self.bird.height):
                self.curr_screen = 'gameover'
        
        # gravity ---- might make a function later
        self.bird.y += self.gravity


    def drawGamePlay(self):
        background = pygame.image.load('sprites/background-day.png').convert()
        background = pygame.transform.scale(background, (self.window_w, self.window_h))
        self.window.blit(background, (0,0))
        self.window.blit(self.bird.image, (self.bird.x, self.bird.y))


    def updateGameOver(self):
        hovered = self.button_rect.collidepoint(self.mouse_pos)
        
        if hovered:
            self.active = True
            print('hovering button')

        if hovered and self.mouse_click[0]:
            print('button clicked')

            # will do later

        
        
        


    def drawGameOver(self):
    
        # game over screen
        game_over_screen = Sprite('sprites/gameover.png')
        center_x = (self.window_w - game_over_screen.width) // 2
        center_y = (self.window_h - game_over_screen.height) // 2
        self.window.blit(game_over_screen.image, (center_x, center_y))

        # play again button
        
        text = 'Play Again?'
        text_color = (255,255,255)
        button_x = center_x + (game_over_screen.width // 4)
        button_y = center_y + 80
        self.button_rect = pygame.Rect(button_x, button_y, 100, 40)

        self.color = self.hover_color if self.active else self.button_color
        pygame.draw.rect(self.window, self.color, self.button_rect, border_radius=5)

        text_surface = self.font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.window.blit(text_surface, text_rect)




game = Game(1000,1000)
