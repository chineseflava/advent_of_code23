import math
import os
import numpy as np

def process_data():
    # read data
    with open('inputs/aoc8_test.txt') as data:
        lines = data.readlines()
   # print(lines)
    
    # variables
    score = 0
    row_size = len(lines[0].strip("\n"))
    column_size = len(lines)
    matrix = np.zeros((row_size,column_size))
    #print(matrix)

    # process lines.
    for idx, line in enumerate(lines):
        row_list = list(line.strip("\n"))
        float_row_list = [int(x) for x in row_list]
        #print(float_row_list)
        row = np.array([float_row_list])
        matrix[idx] = row
    #print(matrix)
    en_matrix = 0
    for x, i in enumerate(matrix):
        for y, j in enumerate(matrix[x]):
            directions = []
            left = matrix[x][y+1:]
            right = np.flip(matrix[x][:y])
            up = matrix[:, y][x+1:]
            down = np.flip(matrix[:, y][:x])
            directions.append(left)
            directions.append(right)
            directions.append(down)
            directions.append(up)
            #print(f"new{down}")
            value = matrix[x,y]
            #print(left, right, up, down, value)
            scenic_score = 0
            score_list = []
            for item in directions:
                #print("item")
                internal_score_list = []
                if len(item) == 0:
                    pass
                else:
                    for idx, s_val in enumerate(item):
                        check = value-s_val
                        if check <= 0:
                            internal_score_list.append(idx+1)
                        elif idx+1 == len(item):
                            internal_score_list.append(idx+1)

                    score_list.append(internal_score_list[0])
            scenic_score = np.prod(score_list)
            if scenic_score >= score:
                score = scenic_score
                print(score_list)
                print(f"{x}, {y} = {value} - score: {score}")
                    
                        

                            #print(f"break at {idx+1}")
                            
                            
                            #print(idx)
                    #print(f"{x}, {y} = {value}")
                    #print(score)

                # if value > max(item, default=-1):
                #     score += 1
                #     #print(f"{x}, {y} = {value}")
                #     break


    #return something
    print(score)
    return score


if __name__ == '__main__':
    process_data()