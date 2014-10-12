# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:42:40 2014

@author: elena & BRANDON CHIOUUUUUUUU
"""

import pygame, math, os, sys
Clock = pygame.time.Clock()
deltat = Clock.tick(30)

class Snake(pygame.sprite.Sprite):
    """Snake character"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snake.png')
        self.pellets = 0   
    def LoadSprites(self):
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))

class MainFrame:
    """Initializes and creates game"""
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        self.LoadSprites()        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.snake_sprites.draw(self.screen)


         
if __name__ == "__main__":
    MainWindow = MainFrame(560, 560)
    MainWindow.MainLoop()

        
pygame.display.update()
