# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014

@author: elena
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

#class Vines:
#    """creates vine maze"""
def createvines():
    vine = pygame.image.load('vine.jpg').convert()    
    for i in range(6):
        MainWindow.screen.blit(vine,(i*16+50,100))

#class Update:
#    MainWindow.screen.blit(MainWindow.background,(0,0)) 
#    pygame.display.flip()

if __name__ == "__main__":
    MainWindow = MainFrame(560, 560) 
    MainWindow.background.fill(color)
    MainWindow.screen.blit(MainWindow.background,(0,0))        
    createvines()
    pygame.display.flip() 
    MainWindow.MainLoop()
    pygame.display.update()
    Clock.tick(60)
    




