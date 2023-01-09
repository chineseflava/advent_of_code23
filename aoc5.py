import math
import os
try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest


def process_data():
    filename = 'inputs/aoc5_moves.txt'
    stacks = ["PDQRVBHF", "VWQZDL", "CPRGQZLH", "BVJFHDR", "CLWZ", "MCGTNPRJ", "SBMVLRJ", "JPD","VWNCD"]
    # for i in range(9):
    #     stacks.append([])
    # stacks[0] = "PDQRVBHF"
    # stacks[1] = "VWQZDL"
    # stacks[2] = "CPRGQZLH"
    # stacks[3] = "BVJFHDR"
    # stacks[4] = "CLWZ"
    # stacks[5] = "MCGTNPRJ"
    # stacks[6] = "SBMVLRJ"
    # stacks[7] = "JPD"
    # stacks[8] = "VWNCD"
    for n in range(9):
        stacks[n] = [*stacks[n][::-1]]
    # variables
    score = 0
    

    data = open('inputs/aoc5_moves.txt', 'r')
    lines = data.readlines()
    

    for item in lines:
        move = item.strip().split(" ")
        from_no = int(move[3])-1
        to_no = int(move[5])-1
        move_no = int(move[1])
        boxes = stacks[from_no][-move_no:]
        stacks[from_no] = stacks[from_no][:-move_no]
        # print(boxes)
        for item in boxes:
            stacks[to_no].append(item)
        # print(stacks[to_no])
        
        # print(stacks[from_no])
       
    result = ""
    for item in stacks:
        result += item.pop()
    print(result)

if __name__ == '__main__':
    process_data()