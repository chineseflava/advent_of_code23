import math
import os
import numpy as np

def process_data():
    # read data
    with open('inputs/aoc9.txt') as data:
        lines = data.readlines()
    
    # variables
    score = 0
    column_size = 1000
    row_size = column_size
    
    matrix = np.zeros((column_size,row_size))
    h_pos = [int(column_size/2), int(row_size/2)]
    t_pos = []
    tail_length = 10
    for n in range(tail_length):
        t_pos.append([int(column_size/2), int(row_size/2)])
    #print(t_pos)
    # process lines.
    #matrix[t_pos[tail_length-1][0], t_pos[tail_length-1][1]] = 1
    for line in lines:
        line.strip()
        direction = line[0]
        steps = int(line[2:])
        print(direction, steps)
        for n in range(steps):
            prev_h_pos = [h_pos[0], h_pos[1]]
            if direction == "U":
                h_pos[1] += 1
            elif direction == "D":
                h_pos[1] -= 1
            elif direction == "L":
                h_pos[0] -= 1
            elif direction == "R":
                h_pos[0] += 1
            #print(f"h: {h_pos}")
            #print(f"t: {t_pos}")
            #print(t_pos[0])
            matrix[t_pos[-1][0], t_pos[-1][1]] = 1
            d_ht = math.sqrt((h_pos[0]-t_pos[0][0])*(h_pos[0]-t_pos[0][0])+(h_pos[1]-t_pos[0][1])*(h_pos[1]-t_pos[0][1]))
            dx = h_pos[0]-t_pos[0][0]
            dy = h_pos[1]-t_pos[0][1]
            
            dist = abs(dx)+abs(dy)
            if dist >= 2:
                if dx == 2:
                    t_pos[0][0] += 1
                    if dy == 1:
                        t_pos[0][1] += 1
                    elif dy == -1:
                        t_pos[0][1] -= 1
                if dy == 2:
                    t_pos[0][1] += 1
                    if dx == 1:
                        t_pos[0][0] += 1
                    elif dx == -1:
                        t_pos[0][0] -= 1
                if dx == -2:
                    t_pos[0][0] -= 1
                    if dy == 1:
                        t_pos[0][1] += 1
                    elif dy == -1:
                        t_pos[0][1] -= 1
                if dy == -2:
                    t_pos[0][1] -= 1
                    if dy == 1:
                        t_pos[0][0] += 1
                    elif dy == -1:
                        t_pos[0][0] -= 1

                #t_pos[0] = [prev_h_pos[0], prev_h_pos[1]]
            
            for i in range(len(t_pos)-1):
                dx = t_pos[i][0]-t_pos[i+1][0]
                dy = t_pos[i][1]-t_pos[i+1][1]
                dist = abs(dx)+abs(dy)
                if dist >= 2:
                    if dx == 2:
                        t_pos[i+1][0] += 1
                        if dy == 1:
                            t_pos[i+1][1] += 1
                        elif dy == -1:
                            t_pos[i+1][1] -= 1
                    if dy == 2:
                        t_pos[i+1][1] += 1
                        if dx == 1:
                            t_pos[i+1][0] += 1
                        elif dx == -1:
                            t_pos[i+1][0] -= 1
                    if dx == -2:
                        t_pos[i+1][0] -= 1
                        if dy == 1:
                            t_pos[i+1][1] += 1
                        elif dy == -1:
                            t_pos[i+1][1] -= 1
                    if dy == -2:
                        t_pos[i+1][1] -= 1
                        if dy == 1:
                            t_pos[i+1][0] += 1
                        elif dy == -1:
                            t_pos[i+1][0] -= 1
            matrix[t_pos[tail_length-1][0], t_pos[tail_length-1][1]] = 1


                # d_tt = math.sqrt((t_pos[i][0]-t_pos[i+1][0])**2+(t_pos[i][1]-t_pos[i+1][1])**2)
                # print(d_tt)
                # print(f"before:{t_pos[i+1]}, previous tail is: {t_pos[i]}")
                # if d_tt > math.sqrt(2):
                #     t_temp = [t_pos[i+1][0], t_pos[i+1][1]]
                #     t_pos[i+1] = [prev_t_pos[0], prev_t_pos[1]]
                #     prev_t_pos = [t_temp[0], t_temp[1]]

                #     #prev_t_pos = [t_temp[0], t_temp[1]]
                # print(f"after:{t_pos[i+1]}")
            

            #print(t_pos[1])
    #print(matrix)
    score = sum(sum(matrix))

    #return something
    print(matrix)
    print(score)
    return score


if __name__ == '__main__':
    process_data()