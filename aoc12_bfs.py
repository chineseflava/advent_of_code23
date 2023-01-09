import math
import os
import sys
import numpy as np
import queue
#import matplotlib.pyplot as plt
#from collections import deque

class DNode():
    def __init__(self, position, distance, children, parent=None):
        self.children = children
        self.position = position
        self.distance = distance
        self.parent = parent

    def has_parent(self):
        if self.parent == None:
            return False
        else:
            return True

    def get_distance(self):
        n = 0
        node = self
        while node.has_parent():
            n += 1
            node = node.parent
        return n

    @property
    def size(self):
        return self.distance



def process_data():
    # read data
    with open('inputs/aoc12.txt') as data:
        lines = [line.rstrip("\n") for line in data]

    # variables # ASCII-values: A=65, a=97
    #print(lines)
    score = 0
    columns = len(lines[0])
    rows = len(lines)
    #print(column_size, row_size)
    grid = {}
    # process lines.
    for j, line in enumerate(lines):
        for i, letter in enumerate(line):
            if letter == "S":
                grid[(i,j)] = 1
                start_pos = (i,j)
            elif letter == "E":
                grid[(i,j)] = 26
                end_pos = (i,j)
            else:
                grid[(i,j)] = ord(letter)-96
                #print(f"{letter} - {ord(letter)}")
    #print(grid)
    graph = {}
    nodes = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for pos in grid:
        children = []
        x, y = pos[0], pos[1]
        for dx, dy in directions:
            next_x, next_y = x+dx, y+dy
            if next_x >= 0 and next_x < columns and next_y >= 0 and next_y < rows:
                next_pos = (next_x, next_y)
                next_val = grid[next_pos]
                if next_val <= grid[pos]+1 or next_val == grid[pos]:
                    children.append(next_pos)
        graph[pos] = children #DNode(pos, math.inf, children)

    def find_shortest_path(start_pos, graph):
        frontier = queue.Queue()
        frontier.put(start_pos)
        came_from = dict()
        came_from[start_pos] = None
        # reached = set()
        # reached.add(start_pos)
        # print(end_pos)

        while not frontier.empty():
            current = frontier.get()
            for next in graph[current]:
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current
        #print("i made it here!")

        current = end_pos
        path = []
        while current != start_pos:
            path.append(current)
            try:
                current = came_from[current]
            except KeyError:
                return 1000

        return len(path)
    
    paths = []
    for item in graph:
        if grid[item] == 1:
            paths.append(find_shortest_path(item, graph))
            #print(paths)
    print(min(paths))
    #return something
    print(score)
    return score


if __name__ == '__main__':
    process_data()