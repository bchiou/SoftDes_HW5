# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import pygame, sys, random
from pygame.locals import *

Clock = pygame.time.Clock()
color = 0,160,255 #color of GUI background
HEIGHT = 560
WIDTH = 560


class MainFrame:
    """Initializes and creates game window.
        Makes sure window will close when the
        Quit button is pressed."""
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
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

class MakeMaze:
    """calculates a maze path using the node points at which
        the maze will change directions"""
    def __init__(self):
        self.state = 'up'
        self.width = WIDTH
        self.height = HEIGHT
    
    def turn_R(self, pos, step):
        return (pos[0] + step, pos[1])

    def turn_L(self, pos, step):
        return (pos[0] - step, pos[1])
        
    def go_up(self, pos, step):
        return (pos[0], pos[1] - step)
    
    def build_maze(self, start, end, steprange): 
        """Builds exactly one randomized path leading from the starting 
        point (x coordinate) to the end point (y coordinate),
        and outpits a list of nodes based on the stepincreases of
        (min steprange, max steprange)"""
    
        self.directions = [self.turn_R, self.turn_L, self.turn_L, self.go_up]
        currentpos = (start, self.height-20)
        list_of_points = [currentpos]
    
        if currentpos[1] == 0 and currentpos[0] == 0:
            return list_of_points
        #Before the end point is reached, move in a random direction
        while currentpos[1] > end or currentpos[0] > end:
            f = random.choice(self.directions)
            currentpos = f(currentpos, random.randint(steprange[0], steprange[1]))
            
            #Check if the vine is out of bounds
            if currentpos[0] < 0:
                currentpos = (0, currentpos[1])
            if currentpos[0] > self.width:
                currentpos = (self.width-20, currentpos[1])
            if currentpos[1] < 0:
                currentpos = (currentpos[0], 0)
            #Add the point to the list of points the vine goes through
            list_of_points.append(currentpos)
        return list_of_points

    def dead_ends(self):
        """Creates random additional deadend vines that are not solutions"""
        rn_W = random.randint(int(self.width*.1), 560) #start 10% up from bottom of screen
        rn_H = random.randint(0, 560)
        return self.build_maze(rn_W, rn_H, (20, 32))


class Vines:
    """Draws vine rectangles using inputted node points"""
    def __init__(self, vcolor = (0,150,100)):
        self.color = vcolor
        self.width = WIDTH
        self.height = HEIGHT
    
    def increasepix(self, obj):
        """Increase thickness of the vine"""
        if obj < 0:
            newobj = obj-20
            return int(newobj)
        if obj >= 0:
            newobj = obj+20
            return int(newobj)

    def drawSolu(self):
        """Draw the correct solution path outputted above from 'build_maze'"""                    
        vinemaze = MakeMaze()
        solulist = vinemaze.build_maze(self.width-20, 0, (20,32))
        
        #draw starting point square at bottom right corner
        start = pygame.Rect(self.width, self.height, -20, -20)
        pygame.draw.rect(MainWindow.background, self.color, start)
        dimenlist = []
        
        #determine the rectangle's starting coordinate, width, and height
        for i in range(1, len(solulist)):
            cur_coord = solulist[i]
            prev_coord = solulist[i-1]
            RectW = prev_coord[0] - cur_coord[0]
            RectH = prev_coord[1] - cur_coord[1]

            #keep track of coordinates where non-overlapping vines occur            
            if RectH > 0:
                dimenlist.append(prev_coord)

            #Increase thickness of vines, depending on if they lie vertical or horizontal            
            if abs(RectW) < abs(RectH):
                newRectW = self.increasepix(RectW)
                vine = pygame.Rect(cur_coord[0], cur_coord[1], newRectW, RectH)              
            else:
                newRectH = self.increasepix(RectH)
                vine = pygame.Rect(cur_coord[0], cur_coord[1], RectW, newRectH)
            pygame.draw.rect(MainWindow.background, self.color, vine)
        
        #fill in the missing corners due to non-overlapping vines
        for i in range(1, len(dimenlist)):
            prevW = dimenlist[i][0]
            prevH = dimenlist[i][1]
            if prevW > 0:
                fillcoord = (prevW, prevH)
                fill = pygame.Rect(fillcoord[0], fillcoord[1], 20, 20)
                pygame.draw.rect(MainWindow.background, self.color, fill)

        MainWindow.screen.blit(MainWindow.background,(0,0))
        pygame.display.update()
        
    def drawDead(self):
        """Draw vines to the list of deadend nodes assigned under 'dead_ends'"""
        vinemaze = MakeMaze()
        
        #draw 5 deadend vines
        for x in xrange(5):  
            mazelist = vinemaze.dead_ends()
            dimenlist = []
            #determine the rectangle's starting coordinate, width, and height
            for j in range(1, len(mazelist)):
                coord = mazelist[j]
                precoord = mazelist[j-1]
                RectW2 = precoord[0] - coord[0]
                RectH2 = precoord[1] - coord[1]
                
                #keep track of coordinates where non-overlapping vines occur            
                if RectH2 > 0:
                    dimenlist.append(precoord)                
                
                
                 #Increase thickness of vines, depending on if they lie vertical or horizontal 
                if abs(RectW2) < abs(RectH2):
                    newRectW2 = self.increasepix(RectW2)
                    vine2 = pygame.Rect(coord[0], coord[1], newRectW2, RectH2)
                    pygame.draw.rect(MainWindow.background, self.color, vine2)
                else:
                    newRectH2 = self.increasepix(RectH2)
                    vine2 = pygame.Rect(coord[0], coord[1], RectW2, newRectH2)
                    pygame.draw.rect(MainWindow.background, self.color, vine2)
                
            #fill in the missing corners due to non-overlapping vines
            for n in range(1, len(dimenlist)):
                prevW = dimenlist[n][0]
                prevH = dimenlist[n][1]
                if prevW > 0:
                    fillcoord = (prevW, prevH)
                    fill = pygame.Rect(fillcoord[0], fillcoord[1], 20, 20)
                    pygame.draw.rect(MainWindow.background, self.color, fill)
            
            MainWindow.screen.blit(MainWindow.background,(0,0))  
                
        pygame.display.update()


    
def main():
    """generate the random maze and draw it to the GUI background"""
    directions = [MakeMaze.turn_R, MakeMaze.turn_L, MakeMaze.go_up] 
    maze = Vines()
    maze.drawSolu()
    maze.drawDead()  


if __name__ == "__main__":

    #Initiate the GUI interface    
    Clock.tick(60)    
    MainWindow = MainFrame() 
    MainWindow.background.fill(color)
   
    #draw the maze
    main()
    
    #update the GUI screen
    pygame.display.flip() 
    MainWindow.MainLoop()
    pygame.display.update()





