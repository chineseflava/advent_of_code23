import math
import os
import numpy as np

def process_data():
    # read data
    with open('inputs/aoc9_test2.txt') as data:
        lines = data.readlines()
    
    # variables
    score = 0
    column_size = 60
    row_size = 60
    
    matrix = np.zeros((column_size,row_size))
    h_pos = [int(column_size/2), int(row_size/2)]
    t_pos = []
    for n in range(9):
        t_pos.append([int(column_size/2), int(row_size/2)])
    print(t_pos)
    # process lines.
    for line in lines:
        line.strip()
        direction = line[0]
        steps = int(line[2:])
        #print(direction, steps)
        for i in range(steps):
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
            
            d_ht = math.sqrt((h_pos[0]-t_pos[0][0])*(h_pos[0]-t_pos[0][0])+(h_pos[1]-t_pos[0][1])*(h_pos[1]-t_pos[0][1]))
            if d_ht > 1.415:
                t_pos[0] = prev_h_pos
                for n in range(len(t_pos)-1)[:]:
                    t_prev = [t_pos[n][0], t_pos[n][1]]
                    d_tt = math.sqrt((t_pos[n][0]-t_pos[n+1][0])**2+(t_pos[n][1]-t_pos[n+1][1])**2)
                    
                    matrix[t_pos[8][0], t_pos[8][1]] = 1
                    if d_tt > 1.415:
                        t_pos[n+1] = t_prev
                    #print(t_pos[8])
            
                #print(t_pos[0], t_pos[1])
                matrix[t_pos[8][0], t_pos[8][1]] = 1
                # matrix[t_pos[0], t_pos[1]] = 1
                # t_pos = prev_h_pos
                # matrix[t_pos[0], t_pos[1]] = 1
        print(t_pos)
    #print(matrix)
    score = sum(sum(matrix))



        
        

    #return something
    print(score)
    return score


if __name__ == '__main__':
    process_data()