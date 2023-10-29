import matplotlib.pyplot as plt
import numpy as np
import random

def flipCoords(rcpos,LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x,y)

class Ant():
    size = 0.5

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "red" 
        #self.heading = heading

    def getPos(self):
        return self.pos

    def stepChange(self,terrain):
        validMoves = [(1,0), (-1,0),(0,1), (0,-1)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 0:
            return False
        return True
        return(0 <= new_pos[0] < subgrid.shape[0]) and (0 <= new_pos[1] < subgrid.shape[new_pos[0], new_pos[1]] ==0)

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Butterfly():

    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 1

    def getPos(self):
        return self.pos

    def stepChange(self, terrain):
        validMoves = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break
    
    def is_valid_move(self, new_pos, subgrid):
        if not(0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 8:
            return False
        return True

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Frog():
    size = 0.6

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "green" 
        #self.heading = heading

    def getPos(self):
        return self.pos

    def stepChange(self,terrain):
        # validMoves = [(1,0), (-1,0),(0,1), (0,-1)]
        validMoves = [(1,0), (-1,0), (2,0), (-2,0), (3,0), (-3,0), (4,0), (-4,0)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            new_pos = (self.pos[0] + move[0], 0)
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 0:
            return False
        return True
        return(0 <= new_pos[0] < subgrid.shape[0]) and (0 <= new_pos[1] < subgrid.shape[new_pos[0], new_pos[1]] ==0)

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)
        
class Rain:
    def __init__(self, position, grid_size):
        self.position = position
        self.grid_size = grid_size
        self.size = 0.1  # Size of raindrops
        self.color = "blue"  # Color of raindrops

    def fall(self):
        self.position[1] += 1  # Move the raindrop one unit down

    def is_out_of_bounds(self):
        return self.position[1] >= self.grid_size[1]

    def plotMe(self, ax):
        circle = plt.Circle(self.position, self.size, color=self.color)
        ax.add_patch(circle)

class Obstacle:
    def __init__(self, position, obstacle_type):
        self.position = position
        self.obstacle_type = obstacle_type  # "Rock" or "Plant"
        self.size = 1.5  # Size of the obstacle
        self.color = "gray" if obstacle_type == "Rock" else "green"

    def plotMe(self, ax):
        circle = plt.Circle(self.position, self.size, color=self.color)
        ax.add_patch(circle)