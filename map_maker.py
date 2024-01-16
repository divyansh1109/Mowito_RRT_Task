
import numpy as np
import matplotlib.pyplot as plt

class MapGenerator:
    def ObstacleRect(x, y, r, map):
        for angle in range(0, 360):
            for radius in range(0, r):
                obs_x = int(x + radius* np.cos(angle))
                obs_y = int(y + radius * np.sin(angle))
                map[obs_x][obs_y] = 1
        return map


    def Map(self):
        print("Continue with default map or customize your's? Enter d or c \n")
        preference = (input("Enter your preference: "))
        if preference == 'd':
            map = np.zeros((2000, 2000))
            map = self.DefaultMap(map)
            print("Current map (x,y) is of: ", map.shape[1]," X ", map.shape[0])
            start_x, start_y = [int(item) for item in input("Starting point (x y) is: ").split()]
            goal_x, goal_y = [int(item) for item in input("Enter the goal point (x y) is: ").split()]

        elif preference == 'c':
            mapSizex, mapSizey = [int(item) for item in input("Enter mapsize (x then y)").split()]
            n = int(input("No. of obstacles: "))
            map = np.zeros((mapSizey, mapSizex))
            for i in range(1, n+1):
                x, y, r =  [int(item) for item in input(f"Enter the Center and Radius (x y and r) of Obstacle {i} in order: ").split()]
                map = MapGenerator.ObstacleRect(x, y, r, map)
            print("Current map (x,y) is of: ", map.shape[1]," X ", map.shape[0])
            plt.imshow(map, cmap='binary')
            plt.show()
            start_x, start_y = [int(item) for item in input("Starting point (x y): ").split()]
            goal_x, goal_y = [int(item) for item in input("Enter the goal point (x y): ").split()]


        else:
            print("Invalid preference. Please try again.")
            self.Map()

        return [map, start_x, start_y, goal_x, goal_y]
    
    def DefaultMap(self, map):
        vertex = [[100, 100, 50], [450, 250, 50], [600,700,50]]
        for vert in vertex:
            MapGenerator.ObstacleRect(vert[0], vert[1], vert[2], map)
        return map