"""
Created on Sun Oct 12 19:49:18 2014
@author: Elena Shaw & Brandon Chiou
"""

import pygame, sys, random
from pygame.locals import *

Clock = pygame.time.Clock()
color = 0,160,255
HEIGHT = 560
WIDTH = 560

#screen = pygame.display.set_mode((560,560))

class MainFrame:
    """Initializes and creates game"""
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
    """calculate a maze path"""
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
        self.directions = [self.turn_R, self.turn_L, self.turn_L, self.go_up]
        currentpos = (start, self.height-4)
        list_of_points = [currentpos]
    
        if currentpos[1] == 0 and currentpos[0] == 0:
            return list_of_points
        while currentpos[1] > end or currentpos[0] > end:
            f = random.choice(self.directions)
            currentpos = f(currentpos, random.randint(steprange[0], steprange[1]))
            #Check if the vine is out of bounds
            if currentpos[0] < 0:
                currentpos = (0, currentpos[1])
            if currentpos[0] > self.width:
                currentpos = (self.width-4, currentpos[1])
            if currentpos[1] < 0:
                currentpos = (currentpos[0], 0)
            #Add the point to the list of points the vine goes through
            list_of_points.append(currentpos)
        return list_of_points

    def dead_ends(self):
        rn_W = random.randint(int(self.width*.1), 560)
        rn_H = random.randint(0, 560)
        return self.build_maze(rn_W, rn_H, (8, 28))


class Vines:
    """creates vine maze"""
    def __init__(self, vcolor = (0,150,100)):
        self.color = vcolor
        self.width = WIDTH
        self.height = HEIGHT
    
    def increasepix(self, obj):
        if obj < 0:
            newobj = obj-4
            return int(newobj)
        if obj >= 0:
            newobj = obj+4
            return int(newobj)

    def drawSolu(self):
#        vine = pygame.image.load('vine.jpg').convert()                     
        vinemaze = MakeMaze()
        solulist = vinemaze.build_maze(self.width-4, 0, (8,24))
        
        #draw starting point square
        start = pygame.Rect(self.width, self.height, -4, -4)
        pygame.draw.rect(MainWindow.background, self.color, start)
        dimenlist = []
        
        for i in range(1, len(solulist)):
#        for i in range(1, 20):
            cur_coord = solulist[i]
            prev_coord = solulist[i-1]
            RectW = prev_coord[0] - cur_coord[0]
            RectH = prev_coord[1] - cur_coord[1]
            if RectH > 0:
                dimenlist.append(prev_coord)
            if abs(RectW) < abs(RectH):
                newRectW = self.increasepix(RectW)
                vine = pygame.Rect(cur_coord[0], cur_coord[1], newRectW, RectH)              
            else:
                newRectH = self.increasepix(RectH)
                vine = pygame.Rect(cur_coord[0], cur_coord[1], RectW, newRectH)
            pygame.draw.rect(MainWindow.background, self.color, vine)
        
        #fill in missing corners due to non overlapping rectangles
        for i in range(1, len(dimenlist)):
            prevW = dimenlist[i][0]
            prevH = dimenlist[i][1]
            if prevW > 0:
                fillcoord = (prevW, prevH)
                fill = pygame.Rect(fillcoord[0], fillcoord[1], 4, 4)
                pygame.draw.rect(MainWindow.background, self.color, fill)

        MainWindow.screen.blit(MainWindow.background,(0,0))
        pygame.display.update()
        
    def drawDead(self):
        vinemaze = MakeMaze()
        for x in xrange(10):  
            mazelist = vinemaze.dead_ends()
            for j in range(1, len(mazelist)):
                coord = mazelist[j]
                precoord = mazelist[j-1]
                RectW2 = precoord[0] - coord[0]
                RectH2 = precoord[1] - coord[1]
                
                if abs(RectW2) < abs(RectH2):
                    newRectW2 = self.increasepix(RectW2)
                    vine2 = pygame.Rect(coord[0], coord[1], newRectW2, RectH2)
                    pygame.draw.rect(MainWindow.background, self.color, vine2)
                else:
                    newRectH2 = self.increasepix(RectH2)
                    vine2 = pygame.Rect(coord[0], coord[1], RectW2, newRectH2)
                    pygame.draw.rect(MainWindow.background, self.color, vine2)
            
            MainWindow.screen.blit(MainWindow.background,(0,0))  
                
        pygame.display.update()


    
def main():
    directions = [MakeMaze.turn_R, MakeMaze.turn_L, MakeMaze.go_up] 
    maze = Vines()
#    MainWindow.screen.blit(MainWindow.background,(0,0))        
#    maze.update()
    maze.drawSolu()
    maze.drawDead()
    



if __name__ == "__main__":

    
    Clock.tick(60)    
    MainWindow = MainFrame() 
    MainWindow.background.fill(color)
   
    main()
    
    pygame.display.flip() 
    MainWindow.MainLoop()
    pygame.display.update()