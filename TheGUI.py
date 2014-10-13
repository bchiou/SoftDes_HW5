# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014

@author: elena
"""

import pygame, sys
from pygame.locals import *
Clock = pygame.time.Clock()

class MainFrame:
    """Initializes and creates game"""
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):      
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
if __name__ == "__main__":
    MainWindow = MainFrame(560, 560)
    MainWindow.MainLoop()


pygame.display.update()
Clock.tick(60)


