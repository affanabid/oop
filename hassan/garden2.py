"""
garden.py - Contains Classes of Animals and Obstacles
        Name : Hasan Waraich
    Student-ID : 21649374
            Fundamentals of Programming - COMP1005
                        Assignment
                                    """
import matplotlib.pyplot as plt
import numpy as np
import random


def flipCoords(rcpos, LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x, y)


class Ant:
    size = 0.2

    def __init__(self, name, pos):
        self.pos = pos
        self.name = name
        self.color = "brown"

    def getPos(self):
        return self.pos

    def stepChange(self, terrain):
        validMoves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = ((self.pos[0]) + move[0], self.pos[1] + move[1])
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 0:
            return False
        return True
        return (0 <= new_pos[0] < subgrid.shape[0]) and (0 <= new_pos[1] < subgrid.shape[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        # if XYpos[0] != rock_pos[0] and XYpos[1] != rock_pos[1]:
        circle1 = plt.Circle(XYpos, self.size, color=self.color)
        ax.add_patch(circle1)

    def Growth(self):
        self.size *= 1.12


class Butterfly:

    def __init__(self, name, pos, color):
        self.name = name
        self.pos = pos
        self.colour = "yellow"
        self.size = 0.4

    def getPos(self):
        return self.pos

    def stepChange(self, terrain):
        validMoves = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 8:
            return False
        return True

    def Growth(self):
        self.size *= 1.15

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Dog():
    size = 0.75

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "brown"

    def getPos(self):
        return self.pos

    def stepChange(self, terrain):
        validMoves = [(0, 0), (1, 0), (-1, 0), (-2, 0), (3, 0), (-3, 0), (4, 0), (-4, 0)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            new_pos = (new_pos[0] + move[0], 0)
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 0:
            return False
        return True
        return (0 <= new_pos[0] < subgrid.shape[0]) and (0 <= new_pos[1] < subrid.shape[new_pos[0], new_pos[1]] == 0)

    def Growth(self):
        self.size *= 1.18

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Frog:
    size = 0.5

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "green"

    def getPos(self):
        return self.pos

    def stepChange(self, terrain):
        validMoves = [(1, 0), (-1, 0), (2, 0), (-2, 0), (3, 0), (-3, 0), (4, 0), (-4, 0)]
        random.shuffle(validMoves)
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            new_pos = (new_pos[0] + move[0], 0)
            if self.is_valid_move(new_pos, terrain):
                self.pos = new_pos
                break

    def is_valid_move(self, new_pos, subgrid):
        if not (0 <= new_pos[0] < subgrid.shape[0]) or not (0 <= new_pos[1] < subgrid.shape[1]):
            return False
        if subgrid[new_pos[0], new_pos[1]] != 0:
            return False
        return True
        return (0 <= new_pos[0] < subgrid.shape[0]) and (0 <= new_pos[1] < subrid.shape[new_pos[0], new_pos[1]] == 0)

    def Growth(self):
        self.size *= 1.2

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        rectangle1 = plt.Rectangle(XYpos, self.size, height=0.8, color=self.colour)
        ax.add_patch(rectangle1)


class Rain:

    def __init__(self, position, grid_size):
        self.position = position
        self.grid_size = grid_size
        self.size = 0.1  # Raindrop size
        self.color = "blue"  # Raindrop color

    def fall(self, tent_position, tent_size):
        if (
            tent_position[0] <= self.position[0] <= tent_position[0] + tent_size and
            tent_position[1] <= self.position[1] <= tent_position[1] + tent_size
        ):
            return f'raindrop in tent'# Raindrop inside the tent, stop falling

        self.position[1] += 2  # Move the raindrop two units down

    def is_out_of_bounds(self):
        return self.position[1] >= self.grid_size[1]

    def plotMe(self, ax):
        circle1 = plt.Circle(self.position, self.size, color=self.color)
        ax.add_patch(circle1)


class Obstacle:

    def __init__(self, position, obstacle_type):
        self.position = position
        self.obstacle_type = obstacle_type
        self.size = 1.5
        self.color = "gray" if obstacle_type == "Rock" else "green"
        self.shape = "circle" if obstacle_type == "Rock" else "polygon"

    def plotMe(self, ax):
        circle = plt.Circle(self.position, self.size, color=self.color)
        ax.add_patch(circle)


class Tent:
    def __init__(self, position, size):
        self.pos = position
        self.size = size  # Ensure size is always a tuple (width, height)
        self.color = "black"
        self.shape = "square"
    
    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        rectangle = plt.Rectangle(XYpos, self.size, height=0.8, color=self.color)
        ax.add_patch(rectangle)
    # def __init__(self, position, size):
    #     self.pos = position
    #     self.size = 3
    #     self.color = "black"
    #     self.shape = "square"
    
    # def plotMe(self,LIMITS, ax):
    #     XYpos = flipCoords(self.pos, LIMITS)
    #     rectangle = plt.Rectangle(XYpos, self.size, height=0.8, color=self.color)
    #     ax.add_patch(rectangle)
    # def plotMe(self, ax):
    #     plt.plot(self.position,self.size,color=self.color, shape=self.shape)
    #     ax.add_patch(self.shape)


