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
    
class Model:
    def __init__(self, view)
        self.view = view
    class Vines:
        
        #Abstracting for now --- blank background
        
if __name__ == "__main__":
    Clock.tick(60)    
    MainWindow = View() 
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