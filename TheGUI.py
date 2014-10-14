# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import pygame, sys, random
from pygame.locals import *
Clock = pygame.time.Clock()
color = 0,160,255


#screen = pygame.display.set_mode((560,560))

class MainFrame:
    """Initializes and creates game"""
    def __init__(self, width, height):
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

x
class Vines:
    """creates vine maze"""
    def __init__(self):
        self.state = 'idle'
    def update(self):
        if self.state == 'idle':
            print 'Idling'
    def draw(self,screen):
        vine = pygame.image.load('vine.jpg').convert()    
        for i in range(6):
            MainWindow.screen.blit(vine,(i*16+50,100))
    
class char(object):
    def __init__(self, jcolor = "red", jsize = "small"):
        self.color = jcolor
        self.size = jsize
    
    def __str__(self):
        return "Jack is now" + self.color + "and" + self.size

    def move(self, xnew, ynew):
        self.x = xnew
        self.y = ynew


if __name__ == "__main__":
    Clock.tick(60)    
    MainWindow = MainFrame(560, 560) 
    MainWindow.background.fill(color)
    MainWindow.screen.blit(MainWindow.background,(0,0))        
    maze = Vines()
    maze.update()
    maze.draw(MainWindow)
    pygame.display.flip() 
    MainWindow.MainLoop()
    pygame.display.update()

    jack = char(x = 0, y = 0)
    jack.move(5,10)
    print self.x



