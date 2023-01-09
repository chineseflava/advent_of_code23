import math
import os
import numpy as np

def process_data():
    # read data
    with open('inputs/aoc10.txt') as data:
        lines = [line.rstrip("\n").rsplit(" ") for line in data]
        #lines = [line.rsplit(" ") for line in lines]
        cycles = []
        for line in lines:
            for item in line:
                cycles.append(item)
        #print(lines)

    
    # variables
    score = 0

    # process lines.
    x_val = 1
    n_cycles = 1
    check = [20, 60, 100, 140, 180, 220]
    signals = []
    output = ""
    for command in cycles:
        curr_row = n_cycles // 40
        #print(curr_row)
        crt_row = n_cycles - 40*curr_row
        if crt_row in [x_val, x_val+1, x_val+2]:
            output += "#"
        else:
            output += "."
        if command == "addx":
            n_cycles += 1
            
        elif command == "noop":
            n_cycles += 1
        else:
            n_cycles += 1
            x_val += int(command)
            print(f"n_cycles is {n_cycles}, add {command} and value is {x_val}")
        
        #     if n_cycles in check:
        
        #         print(f"cycle {n_cycles} has value: {x_val} and {x_val*n_cycles}")
        #     x_val += int(command[1])
        #     n_cycles += 1
        # elif command == "noop":
        #     n_cycles += 1

        if n_cycles in check:
            signals.append(x_val*n_cycles)
            #print(f"cycle {n_cycles} has value: {x_val} and {x_val*n_cycles}")
        
    print(sum(signals))
    print(output[:39])
    print(output[40:79])
    print(output[80:119])
    print(output[120:159])
    print(output[160:199])
    print(output[200:240])
        

    #return something
    #print(score)
    return score


if __name__ == '__main__':
    process_data()