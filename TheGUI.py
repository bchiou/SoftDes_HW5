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

        

    def MainLoop(self):        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                    
                    sys.exit()

class Vines:
    """creates vine maze"""
    def __init__(self):
        self.state = 'idle'

    def maze(self, complexity, density):
        # Only odd shapes
        shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
        # Adjust complexity and density relative to maze size
        complexity = int(complexity * (5 * (shape[0] + shape[1])))
        density    = int(density * (shape[0] // 2 * shape[1] // 2))
        # Build actual maze
        Z = numpy.zeros(shape, dtype=bool)
        # Make aisles
        for i in range(density):
            x, y = numpy.random.randint(0, shape[1] // 2) * 2, numpy.random.randint(0, shape[0] // 2) * 2
            Z[y, x] = 1
            for j in range(6):
                neighbours = []
                if x > 1:             
                    neighbours.append((y, x - 2))
                if x < shape[1] - 2:  neighbours.append((y, x + 2))
                if y > 1:             neighbours.append((y - 2, x))
                if y < shape[0] - 2:  neighbours.append((y + 2, x))
                if len(neighbours):
                    y_,x_ = neighbours[numpy.random.randint(0, len(neighbours) - 1)]
                    if Z[y_, x_] == 0:
                        Z[y_, x_] = 1
                        Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                        x, y = x_, y_
        return Z
    def update(self):
        if self.state == 'idle':
            print 'Idling'
    def draw(self,screen):
        vine = pygame.image.load('vine.jpg').convert()    
        for i in range(6):
            MainWindow.screen.blit(vine,(i*16+50,100))
    
class char(pygame.sprite.Sprite):
    def __init__(self, jcolor = "red", x, y):
        pygame.sprite.Sprite. 
        self.color = jcolor
        self.size = jsize
        
    def move(self, xnew, ynew):
        self.x = xnew
        self.y = ynew


if __name__ == "__main__":
    Clock.tick(60)    
    MainWindow = MainFrame() 
    MainWindow.background.fill(color)
    maze = Vines()
    maze.maze(.75, .55)
    MainWindow.screen.blit(MainWindow.background,(0,0))        
    maze.update()
    maze.draw(MainWindow)
    pygame.display.flip() 
    MainWindow.MainLoop()
    pygame.display.update()

    jack = char(x = 0, y = 0)
    jack.move(5,10)
    print char.move.x




