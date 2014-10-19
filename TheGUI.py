# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

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
    
#class burn:
#    def burn(self, speed):
#        

class char:
    """ Encodes the state of the paddle in the game """
    def __init__(self):
        self.state = 'idle'
        self.x = 200
        self.y = 200
   
    def draw(self,screen):
        self.jackpic = pygame.image.load('snake.png').convert()        
#        self.color = jcolor
        self.size = 1

        MainWindow.screen.blit(self.jackpic, (self.x, self.y))
        

#class PyGameKeyController:
#    def __init__(self,model):
#        self.model = model
#    
#    def handle_key_event(self,event):
#        if event == pygame.K_LEFT:
#            print 'LEFT!'
#            new_x = Jack.x - 5
#            print new_x
#            MainWindow.screen.blit(char.draw.jackpic,(new_x, Jack.y))
#        if event == pygame.K_RIGHT:
#            print 'right!'
#            self.new.x = char.draw.x + 5
#            print self.new.x
#            MainWindow.screen.blit(jack,(new_x, Jack.y))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, collisions):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snake.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.x = pos[0]; self.y = pos[1]
        self.collisions = collisions
        self.type = 'player'
        self.facing = 'up'
        self.speed = 5
        self.lives = 3
        self.invincible = False
        self.dead = False
        self.paused = False


if __name__ == "__main__":
    Clock.tick(60)    
    MainWindow = MainFrame() 
    Jack = char()
    controller = PyGameKeyController(Jack)
    
    MainWindow.background.fill(color)
#    maze = Vines()


    
#    maze.maze(.75, .20)
    MainWindow.screen.blit(MainWindow.background,(0,0))
    Jack.draw(MainWindow)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                controller.handle_key_event(event.key)
#        maze.update()
#        maze.draw(MainWindow)
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




