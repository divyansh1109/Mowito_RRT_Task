
import numpy as np
import matplotlib.pyplot as plt
from planner import MapPlanner
from map_maker import MapGenerator
from node import RRTNode

def rrt(start, goal, map, iterations, max_allowable_dis):
    start_node = RRTNode(start[0], start[1])
    goal_node = RRTNode(goal[0], goal[1])
    nodes = []
    nodes.append(start_node)  

    current_iterations = 0

    # RRT Logic
    while nodes[-1].x != goal_node.x and nodes[-1].y != goal_node.y and current_iterations < iterations:
        current_iterations += 1

        random_point = map_planner.random_point()
        nearest_node = map_planner.nearest_node(random_point, nodes)
        steered_node = map_planner.steer(nearest_node, random_point, max_allowable_dis)
        goal_dis = map_planner.distance(steered_node, goal_node)       # initializing a random point then finding the nearest node
                                                                    # scaling the random point to a particular dist
        if goal_dis <= max_allowable_dis:
            steered_node = goal_node            # Checking if the goal node lies in the region created by max_allowable_dist
                                                # if yes then setting the steer node to the goal node
        if not map_planner.is_collision_free(nearest_node, steered_node, map):
            steered_node.parent = nearest_node
            nearest_node.children.append(steered_node)
            nodes.append(steered_node)                  # checking for the collision (obstacle avoidance)
                                                        # making a triangle rectangle sort of structure including the nearest node and the steered node
                                                        # then checking if there is any obstacle in that region formed by these three vertices

    # Retrace the path
    solution = map_planner.retrace_path(nodes, start_node)
    return nodes, solution                              # retracing the path because 
                                                        # it is possible that we can deflect from our path because of any child node
                                                        # and it is guaranteed that if we retrace the path through parent nodes we definitley rech to the root node

if __name__ == "__main__":
    map_gene = MapGenerator()
    [map, start_x, start_y, goal_x, goal_y] = map_gene.Map()

    start = np.array([start_x, start_y])  # (x,y)
    goal = np.array([goal_x, goal_y])  # (x,y)

    iterations = 500
    max_allowable_dis = 50

    map_planner = MapPlanner(map=map, start=start, goal=goal, iterations=iterations, max_allowable_dis=max_allowable_dis)

    nodes, path = rrt(start, goal, map, iterations, max_allowable_dis)

    fig = plt.figure("RRT Algorithm")
    plt.imshow(map, cmap='binary')
    plt.plot(start[0], start[1], 'ro')
    plt.plot(goal[0], goal[1], 'bo')

    for node in nodes:
        plt.plot(node.x, node.y, 'ro')        # finally plotting all the nodes and the desired path

    map_planner.plot_path(path)
    plt.show()
