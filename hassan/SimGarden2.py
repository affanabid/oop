"""
SimGarden.py - Contains main function of Program
        Name : Hasan Waraich
    Student-ID : 21649374
            Fundamentals of Programming - COMP1005
                        Assignment
                                    """
import matplotlib.pyplot as plt
import numpy as np
from garden2 import *
import csv

def getSubgrid(t, pos):
    rmin = pos[0]-1
    rmax = pos[0]+2
    cmin = pos[1]-1
    cmax = pos[1]+2
    print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax, cmin:cmax]
    return sub

def main():
    LIMITS = (45, 45)
    print("Welcome to the Secret Garden!\n")
    print("LIMITS ARE: ", LIMITS)

    terrain = np.zeros(LIMITS)

    ant_list = []
    num_ants = 5
    spacing = LIMITS[0] // (num_ants + 1)
    for i in range(num_ants):
        ant_position = (35, spacing * (i + 1))
        ant_name = f"A{i + 1}"
        ant_instance = Ant(ant_name, ant_position)
        ant_list.append(ant_instance)

    bfly_list = []
    num_bfly = input("How many Butterflies do you want to see in your Secret Garden? ")
    num_bfly = str(num_bfly)
    spacing = LIMITS[0] // (int(num_bfly)+1)
    for i in range(int(num_bfly)):
        bfly_position = (8, spacing * (i+2))
        bfly_name = f"B{i+1}"  # what is this
        bfly_instance = Butterfly(bfly_name, bfly_position, "yellow")
        bfly_list.append(bfly_instance)

    dog_list = []
    num_dogs = input("How many dogs do you want to put in your Secret Garden? ")
    num_dogs = str(num_dogs)
    spacing = LIMITS[0] // (int(num_dogs)+1)
    for i in range(int(num_dogs)):
        dog_position = (13, spacing * (i+1))
        dog_name = f"A{i+1}"
        dog_instance = Dog(dog_name, dog_position)
        dog_list.append(dog_instance)

    frog_list = []
    num_frog = 4
    spacing = LIMITS[0] // (num_frog+1)  # what is this
    for i in range(num_frog):
        frog_position = (13, spacing * (i+1))
        frog_name = f"A{i+1}"
        frog_instance = Frog(frog_name, frog_position)
        frog_list.append(frog_instance)

    rain_list1 = []
    rain_list2 = []
    rain_list3 = []
    rain_list4 = []
    rain_list5 = []
    num_raindrops = 40
    for _ in range(num_raindrops):  # what is this _
        x1 = random.randint(1, LIMITS[0])
        x2 = random.randint(1, LIMITS[0])
        x3 = random.randint(1, LIMITS[0])
        x4 = random.randint(1, LIMITS[0])
        x5 = random.randint(1, LIMITS[0])
        y1 = -1
        y2 = 0
        y3 = 1
        y4 = 3
        y5 = 4
        raindrop1 = Rain([x1, y1], LIMITS)
        raindrop2 = Rain([x2, y2], LIMITS)
        raindrop3 = Rain([x3, y3], LIMITS)
        raindrop4 = Rain([x4, y4], LIMITS)
        raindrop5 = Rain([x5, y5], LIMITS)
        rain_list1.append(raindrop1)
        rain_list2.append(raindrop2)
        rain_list3.append(raindrop3)
        rain_list4.append(raindrop4)
        rain_list5.append(raindrop5)

    obstacle_list = []
    num_obstacles = 10
    for _ in range(num_obstacles):
        obstacle_type = random.choice(["Rock", "Plant"])
        if obstacle_type == "Rock":
            x = random.randint(0, LIMITS[0] - 1)
            y = random.randint(15, LIMITS[0] - 1)
        else:
            x = random.randint(0,LIMITS[0] - 1)
            y = 12
        coordinates_obstacle = [x, y]
        obstacle = Obstacle([x, y], obstacle_type)
        obstacle_list.append(obstacle)

    tent_list = []
    num_tents = 1
    x = random.randint(40, LIMITS[0])
    y = 9
    # tent_position = [(40, 9), (35, 10)]
    tent_position = (7, 0.2)
    tent_size = 3
    tent_instance = Tent(tent_position, tent_size)
    tent_list.append(tent_instance)

    num_timestamps = 2
    for step in range(num_timestamps):
        terrain = np.genfromtxt('garden3.csv', delimiter=",")
        plt.figure(figsize=(8, 8))
        ax = plt.axes()
        ax.set_aspect("equal")
        plt.imshow(terrain, cmap='terrain_r')

        print("\nObstacle  ################")
        obstacle_positions = []
        for obstacle in obstacle_list:
            obstacle_positions.append(obstacle.position)
            obstacle.plotMe(ax)
        print(obstacle_positions)

        print("\nAnt ###################\n")
        for ant in ant_list:
            if ant.pos not in obstacle_positions:
                ant.stepChange(terrain)
                ant.plotMe(ax, LIMITS)
                ant.Growth()
            """ 
            if ant.pos() == coordinates_obstacle:
                            ant.pos != coordinates_obstacle 
                            """

        print("\nButterfly ###################\n")
        for bfly in bfly_list:
            print(bfly.pos)
            if bfly.pos not in obstacle_positions:
                bfly.stepChange(terrain)
                bfly.plotMe(ax, LIMITS)
                bfly.Growth()

        print("\nFrog ########################")
        for frog in frog_list:
            frog.stepChange(terrain)
            frog.plotMe(ax, LIMITS)
            frog.Growth()

        print("\nMonkey #######################")
        for dog in dog_list:
            dog.stepChange(terrain)
            dog.plotMe(ax, LIMITS)
            dog.Growth()

        print("\nRain Drop ###################")
        for raindrop in rain_list1:
            raindrop.fall(tent_position, tent_size)
            if raindrop.is_out_of_bounds():
                rain_list1.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list2:
            raindrop.fall(tent_position, tent_size)
            if raindrop.is_out_of_bounds():
                rain_list2.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list3:
            raindrop.fall(tent_position, tent_size)
            if raindrop.is_out_of_bounds():
                rain_list3.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list4:
            raindrop.fall(tent_position, tent_size)
            if raindrop.is_out_of_bounds():
                rain_list4.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list5:
            raindrop.fall(tent_position, tent_size)
            if raindrop.is_out_of_bounds():
                rain_list5.remove(raindrop)
            raindrop.plotMe(ax)

        
        for tent in tent_list:
            tent.plotMe(ax, LIMITS)            


        plt.title(f"Time Step {step+1}", fontsize="18")
        plt.grid()
        plt.show()
        # plt.pause(1)
        # plt.cla()

if __name__ == "__main__":
    main()
