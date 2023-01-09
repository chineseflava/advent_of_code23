import math
import os
import numpy as np

def process_data():
    # read data
    with open('inputs/aoc8_test.txt') as data:
        lines = [line.rstrip("\n") for line in data]
    
    # variables
    score = 0

    # process lines.
    for line in lines:
        line.strip()

    #return something
    print(score)
    return score


if __name__ == '__main__':
    process_data()