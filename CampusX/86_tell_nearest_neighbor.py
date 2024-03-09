'''
Write a program that accepts neighbors(set of 2D co-ordinates) and a point(single 2D co-ordinate) and tells nearest neighbor(in terms of euclidean distance)
'''

import math

def nearest_neighbor(neighbors, point):
    min_distance = float('inf')
    nearest = None

    for neighbor in neighbors:
        distance = math.sqrt((neighbor[0] - point[0])**2 + (neighbor[1] - point[1])**2)

        if distance < min_distance:
            min_distance = distance
            nearest = neighbor

    return nearest

neighbors = [(1, 2), (3, 4), (5, 6)]
point = (2, 2)
print(nearest_neighbor(neighbors, point))
