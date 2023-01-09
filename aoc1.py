import math
import os


def find_max_elf(data):

    lines = data.readlines()
    sum_list = []
    temp_sum = 0
    for item in lines:
        if item != '\n':
            temp_sum += int(item)
        else:
            sum_list.append(temp_sum)
            temp_sum = 0
    sum_list.sort(reverse=True)
    max = sum_list[0]
    triple_max = sum(sum_list[0:3])
    return max, triple_max


def main ():
    data = open('inputs/aoc1.txt', 'r')
    max, triple_max = find_max_elf(data)
    print(max)
    print(triple_max)
    

if __name__ == '__main__':
    main()