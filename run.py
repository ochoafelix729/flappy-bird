import pygame
from pygame import *
import sys

class Sprite():
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class Bird():
    def __init__(self, x=500, y=500):
        self.image = pygame.image.load('sprites/bluebird-upflap.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.velocity = 0
        self.jump_time = 0
        # self.do_follow_up = False
        self.falling = True
        self.jumpforce = -8

    def udpateFlap(self):
        if (pygame.time.get_ticks() - self.jump_time) < 500:
            self.image = pygame.image.load('sprites/bluebird-downflap.png')

        elif self.velocity < 0:
            self.image = pygame.image.load('sprites/bluebird-midflap.png')
        
        elif self.velocity > 0:
            self.image = pygame.image.load('sprites/bluebird-upflap.png')
        


class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h
        self.gravity = 0.5
        self.gravity_on = True
        self.curr_screen = 'intro'
        
        # create window
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        pygame.display.set_caption('Flappy Bird')

        # draw background
        self.background = pygame.image.load('sprites/background-day.png').convert()
        self.background = pygame.transform.scale(self.background, (self.window_w, self.window_h))
        self.window.blit(self.background, (0,0))

        # for gameplay screen
        self.bird = Bird()
        self.base = None
        self.base_height = 688
        self.bird.start_x = 500 - (self.bird.width // 2)
        self.bird.start_y = 445 - (self.bird.height // 2)
        self.bird.x = self.bird.start_x
        self.bird.y = self.bird.start_y

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

            print(self.gravity_on)

            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_click = pygame.mouse.get_pressed()

            self.handleEvents()

            if self.curr_screen == 'intro':
                self.drawIntro()
                self.updateIntro()

            elif self.curr_screen == 'gameplay':
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

    
    def clearScreen(self):
        self.window.fill((0,0,0))
        self.background = pygame.image.load('sprites/background-day.png').convert()
        self.background = pygame.transform.scale(self.background, (self.window_w, self.window_h))
        self.window.blit(self.background, (0,0))


    def restartGame(self):
        self.bird.x = self.bird.start_x
        self.bird.y = self.bird.start_y


    def drawIntro(self):
        self.clearScreen()
        intro_screen = Sprite('sprites/message.png')
        center_x = (self.window_w - intro_screen.width) // 2
        center_y = (self.window_h - intro_screen.height) // 2
        self.window.blit(intro_screen.image, (center_x, center_y))

    
    def updateIntro(self):
        if abs(self.mouse_pos[0] - 501) <= 20 and abs(self.mouse_pos[1] - 505) <= 20 and self.mouse_click[0]:
            self.curr_screen = 'gameplay'


    def drawGamePlay(self):
        self.clearScreen()
        self.window.blit(self.bird.image, (self.bird.x, self.bird.y))

        # bottom base
        left_base = Sprite('sprites/base.png') # just for looks
        self.base = Sprite('sprites/base.png')
        right_base = Sprite('sprites/base.png') # just for looks

        self.window.blit(left_base.image, (0,self.base_height))
        self.window.blit(self.base.image, (336,self.base_height))
        self.window.blit(right_base.image, (672,self.base_height))


    def updateGamePlay(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity_on = True
            self.bird.velocity = self.bird.jumpforce
            self.bird.jump_time = pygame.time.get_ticks()

        if (pygame.time.get_ticks() - self.bird.jump_time) > 50 and abs(self.bird.y - (self.base_height - self.bird.height)) <= 5:
            self.gravity_on = False
        
        # gravity
        if self.gravity_on:
            self.bird.velocity += self.gravity
            self.bird.y += self.bird.velocity
            self.bird.udpateFlap()


    def drawGameOver(self):
        self.clearScreen()
    
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


    def updateGameOver(self):
        hovered = self.button_rect.collidepoint(self.mouse_pos)
        
        if hovered:
            self.active = True

        if hovered and self.mouse_click[0]:
            self.curr_screen = 'intro'
            self.restartGame()


# start game
game = Game(1008,800)
