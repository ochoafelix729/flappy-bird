import pygame
from pygame import *
import random

class Sprite():
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class Bird():
    def __init__(self):
        self.image = pygame.image.load('sprites/bluebird-upflap.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 0
        self.y = 0
        self.start_x = None
        self.start_y = None
        self.velocity = 0
        self.jump_time = 0
        self.falling = True
        self.jumpforce = -12 # constant
        self.hitbox = self.image.get_rect()

    def udpateFlap(self):
        if (pygame.time.get_ticks() - self.jump_time) < 500:
            self.image = pygame.image.load('sprites/bluebird-downflap.png')

        elif self.velocity < 0:
            self.image = pygame.image.load('sprites/bluebird-midflap.png')
        
        elif self.velocity > 0:
            self.image = pygame.image.load('sprites/bluebird-upflap.png')
        

class Pipe():
    def __init__(self, x):
        self.image = pygame.image.load('sprites/pipe-green.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = 0
        self.on_screen = True
        self.hitbox = self.image.get_rect()

class Game():
    def __init__(self, w, h):

        self.window_w = w
        self.window_h = h
        self.gravity = 0.9 # constant
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
        self.base_height = 688 # constant
        self.bird.start_x = 500 - (self.bird.width // 2) # constant
        self.bird.start_y = 445 - (self.bird.height // 2) # constant
        self.bird.x = self.bird.start_x
        self.bird.y = self.bird.start_y
        self.last_pipe_time = 0
        self.pipes = []
        self.collision_buffer = 0
        self.score = 0
        self.last_score_udpate_time = 0
        

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

            if pygame.time.get_ticks() - self.last_pipe_time > 1500:
                self.generatePipes()
                self.last_pipe_time = pygame.time.get_ticks()

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
        self.pipes.clear()
        self.last_pipe_time = pygame.time.get_ticks()
        


    def generatePipes(self):
        min = 80 # constant - this will increase as game goes on
        max = 300 # constant
        pipe_x = self.window_w

        # create bottom pipe
        bottom_pipe = Pipe(pipe_x)
        bottom_pipe.image = pygame.image.load('sprites/pipe-green.png').convert_alpha()
        bottom_pipe.x = pipe_x
        bottom_pipe.y = random.randint(self.base_height - max, self.base_height - min)

        # create top pipe
        top_pipe = Pipe(pipe_x)
        top_pipe.image = pygame.image.load('sprites/pipe-green-down.png').convert_alpha()
        top_pipe.x = pipe_x
        top_pipe.y = random.randint(min - top_pipe.image.get_height(), max - top_pipe.image.get_height())

        self.pipes.append(top_pipe)
        self.pipes.append(bottom_pipe)


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

        # pipes
        for pipe in self.pipes:
            self.window.blit(pipe.image, (pipe.x, pipe.y))
        
        # bird
        self.window.blit(self.bird.image, (self.bird.x, self.bird.y))

        # base
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

        # screen movement
        for pipe in self.pipes:
            pipe.x -= 10 # constant
            if pipe.x < (-1 * pipe.width):
                pipe.on_screen = False
                self.pipes.remove(pipe)

        # update hitboxes
        self.bird.hitbox = pygame.Rect(self.bird.x, self.bird.y, self.bird.width, self.bird.height)
        for pipe in self.pipes:
            pipe.hitbox = pygame.Rect(pipe.x, pipe.y, pipe.width, pipe.height)

        # collision detection
        for pipe in self.pipes:
            if self.bird.hitbox.colliderect(pipe.hitbox):
                self.curr_screen = 'gameover'

        # score tracker
        proximity_box = Rect(self.bird.x, 0, self.bird.width, self.window_h)
        for pipe in self.pipes:
            if  (pygame.time.get_ticks() - self.last_score_udpate_time) > 390 and proximity_box.colliderect(pipe.hitbox):
                self.score += 0.5
                self.last_score_udpate_time = pygame.time.get_ticks()
                print(self.score if self.score.is_integer() else '')
        
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
        button_y = center_y + 80 # constant

        self.button_rect = pygame.Rect(button_x, button_y, 100, 40) # constant
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
