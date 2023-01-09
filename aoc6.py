import math
import os
import numpy as np


def process_data():
    # read data
    data = open('inputs/aoc6.txt', 'r')
    lines = data.readlines()
    
    # variables
    score = 0
    this_set = set()
    # print(lines)
    # process lines.
    for idx, item in enumerate(lines[0]):
        this_set = set()
        for i in range(14):
            this_set.add(lines[0][idx+i])
            #print(lines[0][i])
        if len(this_set) == 14:
            score = idx+14
            print(score)
            return score
            
        


if __name__ == '__main__':
    process_data()
