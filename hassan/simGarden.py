import matplotlib.pyplot as plt
import numpy as np
from garden import *
import csv

def getSubgrid(t, pos):
    rmin = pos[0]-1
    rmax = pos[0]+2
    cmin = pos[1]-1
    cmax = pos[1]+2
    print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax,cmin:cmax]
    return sub

def main():
    LIMITS = (45,45)
    print("\nWelcome to the Secret Garden...\n")
    print("LIMITS ARE:",LIMITS)

    terrain = np.zeros(LIMITS)

#Frog added
    frog_list = []
    num_frog = 5
    spacing = LIMITS[0] // (num_frog + 1)
    for i in range(num_frog):
        frog_position = (14, spacing * (i+1))
        frog_name = f"A{i+1}"
        frog_instance = Frog(frog_name, frog_position)
        frog_list.append(frog_instance)

    ant_list = []
    num_ants = 5
    spacing = LIMITS[0] // (num_ants + 1)
    for i in range(num_ants):
        ant_position = (35, spacing * (i+1))
        ant_name = f"A{i+1}"
        ant_instance = Ant(ant_name, ant_position)
        ant_list.append(ant_instance)

    bfly_list = []
    num_bfly = 5
    spacing = LIMITS[0] // (num_bfly + 1)
    for i in range(num_bfly):
        bfly_position = (10, spacing * (i+1))
        bfly_name = f"B{i+1}"
        bfly_instance = Butterfly(bfly_name, bfly_position, "yellow")
        bfly_list.append(bfly_instance)

# Rain added
    rain_list = []
    num_raindrops = 40  # Number of raindrops
    for _ in range(num_raindrops):
        x = random.randint(0, LIMITS[0] - 1)  # Random x-coordinate
        y = 0  # Starting at y = 0 (top of the grid)
        raindrop = Rain([x, y], LIMITS)
        rain_list.append(raindrop)

    rain_list1 = []
    rain_list2 = []
    rain_list3 = []
    rain_list4 = []
    rain_list5 = []
    num_raindrops = 40  # Number of raindrops
    for _ in range(num_raindrops):
        x1 = random.randint(1, LIMITS[0])  # Random x-coordinate
        x2 = random.randint(1, LIMITS[0])  # Random x-coordinate
        x3 = random.randint(1, LIMITS[0])
        x4 = random.randint(1, LIMITS[0])
        x5 = random.randint(1, LIMITS[0])
        y1 = 0  # Starting at y = 0 (top of the grid)
        y2 = 1  # Starting at y = 0 (top of the grid)
        y3 = 3
        y4 = 4
        y5 = 5
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


# Obstacles added
    obstacle_list = []
    num_obstacles = 10  # Number of obstacles (rocks and plants)
    for _ in range(num_obstacles):
        obstacle_type = random.choice(["Rock", "Plant"])
        if obstacle_type == 'Rock':
            x = random.randint(0, LIMITS[0] - 1)  # Random x-coordinate
            y = random.randint(15, LIMITS[1] - 1)  # Random y-coordinate
        else:
            x = random.randint(0, LIMITS[0] - 1)
            y = 14
        obstacle = Obstacle([x, y], obstacle_type)
        obstacle_list.append(obstacle)

    num_timestamps = 3
    for step in range(num_timestamps):
        terrain = np.genfromtxt('garden3.csv', delimiter = ',')
        plt.figure(figsize=(8,8))
        ax = plt.axes()
        ax.set_aspect("equal")
        plt.imshow(terrain, cmap = 'terrain_r')

        print("\nAnt ##########################")
        print("\nButterfly ##################")

        for ant in ant_list:
            ant.stepChange(terrain)
            ant.plotMe(ax, LIMITS)
        for bfly in bfly_list:
            bfly.stepChange(terrain)
            bfly.plotMe(ax, LIMITS)

# Additions:
        for frog in frog_list:
            frog.stepChange(terrain)
            frog.plotMe(ax, LIMITS)
        for raindrop in rain_list1:
            raindrop1.fall()
            if raindrop.is_out_of_bounds():
                rain_list.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list2:
            raindrop.fall()
            if raindrop.is_out_of_bounds():
                rain_list2.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list3:
            raindrop.fall()
            if raindrop.is_out_of_bounds():
                rain_list.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list4:
            raindrop.fall()
            if raindrop.is_out_of_bounds():
                rain_list.remove(raindrop)
            raindrop.plotMe(ax)
        for raindrop in rain_list5:
            raindrop.fall()
            if raindrop.is_out_of_bounds():
                rain_list.remove(raindrop)
            raindrop.plotMe(ax)
        for obstacle in obstacle_list:
            obstacle.plotMe(ax)

        plt.title(f"Time Step {step + 1}", fontsize="18")
        plt.grid()
        plt.show()
#        plt.pause(1)
#        plt.cla()

if __name__ == "__main__":
    main()
