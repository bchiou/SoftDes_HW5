"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import numpy
import pygame, sys, random
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
        print self.model.vines.text
        self.screen.fill(color)
        pygame.draw.rect(self.screen, pygame.Color(255,0,0), (self.model.jack.x-10, self.model.jack.y-10, 10, 10))
        pygame.display.update()
#####################################################################        
class Vines: 
    #If this doesn't work, put outside of Model class
    #Abstracting for now --- blank vines
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
    def getinput(self):
        self.model.vines.text = raw_input('Fuck this shit\n')
        
#####################################################################
class Jack:
    def __init__(self):
        self.image = pygame.image.load('snake.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
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
#####################################################################               
if __name__ == "__main__":
    gameModel = Model()
    gameView = View(gameModel)
    gameCont = Controller(gameModel)
    running=True    
    gameCont.getinput()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT: running = False
        gameView.viewprint()
        time.sleep(0.001)
    pygame.quit()