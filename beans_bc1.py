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

class View:
    """Initializes and creates game"""
    def __init__(self):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Jack and the Bean Stalk')
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.view.fill(color)
        #draw model.vines screen.blit(model.vines)
        #This class (View class) will print self.text/the ACTUAL vines
    
class Model:
    def __init__(self):
        self.vines = Vines()
    class Vines: 
        #If this doesn't work, put outside of Model class
        #Abstracting for now --- blank vines
        def __init__(self):
            self.text = '""fucking vines"-that can be interpreted two ways"-Pratool Gadtaula'
            
class Controller:
    def __init__(self, model):
        self.model = model
    
    def getinput(self):
        self.model.vines.text = raw_input('Fuck this shit\n')
        
        
if __name__ == "__main__":