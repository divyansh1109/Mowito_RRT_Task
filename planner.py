
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from node import RRTNode

max_allowable_dis = 50

class MapPlanner:
    def __init__(self, map, start, goal, iterations, max_allowable_dis):
        self.map = map
        self.start = start
        self.goal = goal
        self.iterations = iterations
        self.max_allowable_dis = max_allowable_dis

    def random_point(self):
        x = random.randint(0, self.map.shape[1])
        y = random.randint(0, self.map.shape[0])
        return RRTNode(x, y)

    def nearest_node(self, random_node, nodes):
        distances = [self.distance(random_node, node) for node in nodes]
        return nodes[np.argmin(distances)]

    def steer(self, from_node, to_node, max_distance):
        d = self.distance(from_node, to_node)
        if d < max_distance:
            return to_node
        else:
            theta = np.arctan2(to_node.y - from_node.y, to_node.x - from_node.x)
            new_x = from_node.x + max_distance * np.cos(theta)
            new_y = from_node.y + max_distance * np.sin(theta)
            return RRTNode(new_x, new_y)

    def is_collision_free(self, from_node, to_node, map):
        intersection = False
        new_point_1 = RRTNode(from_node.x, to_node.y)
        new_point_2 = RRTNode(to_node.x, from_node.y)
        for i in range(min(new_point_1.x,to_node.x), max(new_point_1.x,to_node.x)):
            for j in range(min(new_point_1.y,from_node.y), max(new_point_1.y,from_node.y)):
                if map [i][j] == 1:
                    intersection = True
                    break
            if not intersection:
                break
        return intersection

    def distance(self, node1, node2):
        return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

    def retrace_path(self, nodes, start_node):
        solution = []
        goal_node = nodes[-1]
        solution.append(goal_node)
        parent = goal_node.parent
        while solution[-1] != start_node:
            for node in nodes:
                if node == parent:
                    solution.append(node)
                    parent = node.parent
                    break
                else:
                    continue
        return solution

    def plot_path(self, solution):
        previous_node = solution[0]
        for i in range(1, len(solution)):
            next_node = solution[i]
            plt.plot([previous_node.x, next_node.x], [previous_node.y, next_node.y], 'go', linestyle="--")
            previous_node = next_node