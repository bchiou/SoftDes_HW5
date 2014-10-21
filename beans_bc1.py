"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import numpy
import pygame, sys, random, time
from pygame.locals import *
Clock = pygame.time.Clock()
color = pygame.Color(0,160,255)
height = 560
width = 560

#screen = pygame.display.set_mode((560,560))

class View:
    """Initializes and creates game"""
    def __init__(self, model):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.model = model
        pygame.display.set_caption('Jack and the Bean Stalk')
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        #draw model.vines screen.blit(model.vines)
        #This class (View class) will print self.text/the ACTUAL vines

    def viewprint(self):
        #print self.model.vines.text
        self.screen.fill(color)
        pygame.draw.rect(self.screen, pygame.Color(255,0,0), (self.model.jack.x, self.model.jack.y, 10, 10))
        pygame.display.update()
#####################################################################        
class Vines: 
    #Abstracting for now --- INSERT VINE CODE HERE
    def __init__(self):
        self.text = '""fucking vines"-that can be interpreted two ways"-Pratool Gadtaula' 
        
#####################################################################    
class Model:
    def __init__(self):
        self.vines = Vines()
        self.jack = Jack()

#####################################################################                
class Controller:
    def __init__(self, model):
        self.model = model    
    def handle_key_event(self, event):        
        if event.type == KEYUP:
            if event.key == pygame.K_UP:
                if (self.model.jack.y > 0): self.model.jack.y -= 10
            if event.key == pygame.K_DOWN:
                if (self.model.jack.y < height - 10): self.model.jack.y += 10
            if event.key == pygame.K_LEFT:
                if (self.model.jack.x > 0): self.model.jack.x -= 10
            if event.key == pygame.K_RIGHT:
                if (self.model.jack.x < width - 10): self.model.jack.x += 10
            
#####################################################################
class Jack:
    def __init__(self):
        self.x = height - 10
        self.y = width - 10

#####################################################################               
if __name__ == "__main__":
    gameModel = Model()
    gameView = View(gameModel)
    gameCont = Controller(gameModel)
    running=True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT: 
                running = False
            else:
                gameCont.handle_key_event(event)
        gameView.viewprint()
        time.sleep(0.001)
    pygame.quit()