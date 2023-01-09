import math
import os
import numpy as np
from functools import cmp_to_key

try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


# return -1 if l < r, +1 if l>r and 0 otherwise
def compare(left, right):
    #print(left, right)
    for i in range(min(len(left), len(right))):
        #print(left[i], right[i])
        # Both are ints
        if isinstance(left[i],int) and isinstance(right[i], int):
            if left[i] < right[i]: return 1
            if left[i] > right[i]: return -1

        # both are lists
        elif isinstance(left[i],list) and isinstance(right[i], list):
            c = compare(left[i],right[i])
            if c != 0: 
                return c
        
        # one int and one list
        elif isinstance(left[i], int) and isinstance(right[i], list):
            c = compare([left[i]], right[i])
            #if c != 0: 
            return c

        if isinstance(left[i], list) and isinstance(right[i], int):
            c = compare(left[i], [right[i]])
            #if c != 0: 
            return c
    if len(left) < len(right): return 1
    if len(left) > len(right): return -1
    return 0


def process_data():
    # read data
    filename = 'inputs/aoc13.txt'
    N = 3
    score = 0
    indices = []
    input_lst = []
    with open(filename) as f:
        for i, lines in enumerate(grouper(f, N, '')):
            assert len(lines) == N
            left_lines = lines[0].strip()
            right_lines = lines[1].strip()
            
            left = eval(left_lines)
            right = eval (right_lines)
            input_lst.append(left)
            input_lst.append(right)

            #print(left, right)
            #check if sorting is correct, return False if not.
            #print(f"i {i}")
            correct = compare(left, right)
            if correct == 1:
                indices.append(i+1)
                #print(f"correct indices: {indices}")

        score = sum(indices)
    print(f"correct indices: {indices}")

    #return something
    print(f"part 1: {score}")
    #part 2
    input_lst.append([[2]])
    input_lst.append([[6]])
    sorted_list = sorted(input_lst, key=cmp_to_key(compare), reverse=True)

    score2 = 1
    for idx, item in enumerate(sorted_list):
        if item == [[2]]:
            print(f"index of [[2]] is {idx}")
            score2 = score2*(idx+1)
        if item == [[6]]:
            print(f"index of [[6]] is {idx}")
            score2 = score2*(idx+1)
    print(f"part 2: {score2}")
        
        

    return score

    


if __name__ == '__main__':
    process_data()
