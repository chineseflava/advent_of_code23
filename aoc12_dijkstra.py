import math
import os
import sys
import numpy as np
#import matplotlib.pyplot as plt
#from collections import deque

class DNode():
    def __init__(self, position, distance, parent=None):
        self.position = position
        self.distance = distance
        self.parent = parent

    @property
    def size(self):
        return self.distance



def process_data():
    # read data
    with open('inputs/aoc12_test.txt') as data:
        lines = [line.rstrip("\n") for line in data]

    # variables # ASCII-values: A=65, a=97
    print(lines)
    score = 0
    columns = len(lines[0])
    rows = len(lines)
    #print(column_size, row_size)
    grid = {}
    # process lines.
    for j, line in enumerate(lines):
        for i, letter in enumerate(line):
            if letter == "S":
                grid[(i,j)] = 0
                start_pos = (i,j)
            elif letter == "E":
                grid[(i,j)] = 27
                end_pos = (i,j)
            else:
                grid[(i,j)] = ord(letter)-96
                #print(f"{letter} - {ord(letter)}")
    #print(grid)
    unexplored_grid = {}
    for position in grid:
        if position == start_pos:
            unexplored_grid[position] = DNode(position, 0)
        else:
            unexplored_grid[position] = DNode(position, math.inf)
    print(unexplored_grid)
    while len(unexplored_grid) != 0:
        #Get current node.
        current_node = 
        



    #print(end_pos)
    # explored_set = set()
    # explored_set.add(start_pos)
    # explore_deck = deque()
    # explore_deck.appendleft((0, start_pos))
    # directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # while explore_deck:
    #     curr_steps, pos = explore_deck.popleft()
    #     if pos == end_pos:
    #         score = curr_steps
    #         break
    #     x,y = pos
    #     height = grid[pos]
        
    #     for dx, dy in directions:
    #         next_x, next_y = x+dx, y+dy
    #         if next_x < 0 or next_x >= columns or next_y < 0 or next_y >= rows:
    #             continue
    #         next_pos = (next_x, next_y)
    #         if next_pos in explored_set:
    #             continue
    #         next_height = grid[next_pos]
    #         if next_height == height or next_height == height + 1:
    #             steps = curr_steps + 1
    #             explore_deck.append((steps, next_pos))
    #             explored_set.add(next_pos)

    #return something
    print(score)
    return score


if __name__ == '__main__':
    process_data()