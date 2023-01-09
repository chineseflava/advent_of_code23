import math
import os
import numpy as np

def sand_be_drippin_til_no_mo(block_list, floor=None):
    temp_block_list = block_list.copy()
    dripping_sand = True
    while dripping_sand:
        x,y = 500, 0
        blocked = False
        while not blocked:
            #print((x,y))
            if (x,y+1) not in temp_block_list:
                y += 1
            elif (x-1, y+1) not in temp_block_list:
                x -= 1
                y += 1
            elif (x+1, y+1) not in temp_block_list:
                x += 1
                y += 1
            else:
                temp_block_list.add((x,y))
                blocked = True
            if floor:
                if y == floor-1:
                    temp_block_list.add((x,y))
                    blocked = True
                if (500,0) in temp_block_list:
                    dripping_sand = False
            else:
                if y == 500:
                    blocked = True
                    dripping_sand = False
            #print(x,y)
    return len(temp_block_list)-len(block_list)

def process_data():
    # read data
    with open('inputs/joakim_14_data.txt') as data:
        lines = [line.rstrip("\n").split(" -> ") for line in data]
    
    # variables
    score = 0
    block_list = set()

    # process lines.
    floor = 0
    for coords in lines:
        #print(line)
        for i in range(len(coords)):
            if i == 0:
                x,y = eval(coords[i])
                if y > floor: floor = y
                block_list.add((x,y))
            else:
                tox, toy = eval(coords[i])
                if toy > floor: floor = toy
                dx, dy = tox-x, toy-y
                while (tox,toy) != (x,y):
                    if dx > 0: x += 1
                    if dx < 0: x -= 1
                    if dy > 0: y += 1
                    if dy < 0: y -= 1
                    block_list.add((x, y))
    #print(len(block_list))
    floor = floor +2
    print(f"floor: {floor}")
   
    score1 = sand_be_drippin_til_no_mo(block_list)
    score2 = sand_be_drippin_til_no_mo(block_list, floor)
    print(f"part 1: {score1}")
    print(f"part 2: {score2}")

            

    #return something
    #print(score)
    return score


if __name__ == '__main__':
    process_data()