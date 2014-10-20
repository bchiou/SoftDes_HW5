# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import numpy
import pygame, sys, random
from pygame.locals import *
Clock = pygame.time.Clock()
color = 0,160,255
height = 560
width = 560

#screen = pygame.display.set_mode((560,560))

class MainFrame:
    """Initializes and creates game"""
    def __init__(self):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Jack and the Bean Stalk')
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()

class Vines:
    """creates vine maze"""
    def __init__(self):
        self.state = 'idle'

    def maze(self, complexity, density):
        H = height
        W = width        
        # Only odd shapes
        shape = ((H // 2) * 2 + 1, (W // 2) * 2 + 1)
        # Adjust complexity and density relative to maze size
        complexity = int(complexity * ((shape[0] + shape[1])//2))
        density    = int(density * (shape[0] // 2 + shape[1] // 2))
        # Build actual maze
        Z = numpy.zeros(shape, dtype=int)
        # Make aisles
        for i in range(density):
            x, y = numpy.random.randint(0, shape[1] // 2) * 2, numpy.random.randint(0, shape[0] //2) * 2
            Z[y, x] = 1
            for j in range(complexity):
                neighbours = []
                if x > 1:             
                    neighbours.append((y, x - 2))
                if x < shape[1] - 2:  
                    neighbours.append((y, x + 2))
                if y > 1:             
                    neighbours.append((y - 2, x))
                if y < shape[0] - 2:  
                    neighbours.append((y + 2, x))
                if len(neighbours):
                    y_,x_ = neighbours[numpy.random.randint(0, len(neighbours) - 1)]
                    if Z[y_, x_] == 0:
                        Z[y_, x_] = 1
                        Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                        x, y = x_, y_
        return Z
#    def update(self):
#        if self.state == 'idle':
#            print 'Idling'
    def draw(self,screen):
        vine = pygame.image.load('vine.jpg').convert() 
       # Z = self.maze(.75, .20)
        Z=self.maze(1,1)
        V = []
        for i in range(len(Z)):
            for j in range(len(Z)):
#                print Z[i]
#                print Z[j]                
#                print Z[i,j]
                if Z[i][j] != 0: #if Z[i][j]
                    V.append((i*2,j*2))
                    MainWindow.screen.blit(vine, (i*2,j*2))
        return V

class CharControl(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snake.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
#        self.model = model
        self.rect = self.image.get_rect()
        self.x = height
        self.y = width
        self.type = 'player'
        self.facing = 'up'
        self.speed = 5
        self.lives = 3
        self.invincible = False
        self.dead = False
        self.paused = False
        
    def draw(self,screen):
        self.jackpic = pygame.image.load('snake.png').convert()
        self.size = 1
        MainWindow.screen.blit(self.jackpic, (self.x, self.y))
    
    def handle_key_event(self, event):
        if event == pygame.K_LEFT:
            print 'LEFT!'
            if self.x in range (0, height):
                new_x = self.x - 5 #something WRONG here
                print new_x
                MainWindow.screen.blit(self.jackpic,(new_x, Jack.y))
            else:
                #doNOTHING
        if event == pygame.K_RIGHT:
            print 'right!'
            new_y = self.y + 5
            print self.new.x
            MainWindow.screen.blit(self.jackpic,(new_x, Jack.y))
#        if event == pygame.K_UP:
#        
#        if event == pygame.K_DOWN:

if __name__ == "__main__":
    Clock.tick(60)    
    MainWindow = MainFrame() 
#    Jack = char()
    controller = CharControl()
    controller.draw(MainWindow)
    
    MainWindow.background.fill(color)
#    maze = Vines()
#    maze.maze(.75, .20)
    MainWindow.screen.blit(MainWindow.background,(0,0))

#    maze.update()
#    maze.draw(MainWindow)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                controller.handle_key_event(event.key)

        pygame.display.flip() 
        pygame.display.update()
#        Clock.sleep(.001) 
        
#    maze.update()
#    maze.draw(MainWindow)
#    pygame.display.flip() 
#    MainWindow.MainLoop()
#    pygame.display.update()

#    jack = char(x = 0, y = 0)
#    jack.move(5,10)
#    print char.move.x