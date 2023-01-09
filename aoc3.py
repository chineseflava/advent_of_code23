import math
import os

try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def process_data():
    data = open('inputs/aoc3.txt', 'r')
    lines = data.readlines()

    # variables DO NOT OVERWRITE FUNCTIONS
    # ASCII-values: A=65, a=97
    score = 0
    
    
    # extract data from file DONT FORGET TO SAVE THE TXT-FILE
    print("DONT FORGET TO SAVE THE TXT-FILE")
    for item in lines:
        left = item.strip()[0:math.floor(len(item)/2)]
        right = item.strip()[math.floor(len(item)/2):]
        #print(left, right)
        left_set= set()
        right_set= set()
        for letter in left:
            left_set.add(letter)
        for letter in right:
            if letter in left_set and letter not in right_set:
                score += get_priority(letter)
                
            right_set.add(letter)
    print(score)
    return score


def get_priority(letter):
    if letter.isupper():
        priority = ord(letter)-64+26
    elif not letter.isupper():
        priority = ord(letter)-96
    return priority


def process_data2():
    filename = 'inputs/aoc3.txt'

    score = 0
    N = 3
    with open(filename) as f:
        for lines in grouper(f, N, ''):
            assert len(lines) == N
            #print(lines)
            # process N lines here
            first = lines[0].strip()
            second = lines[1].strip()
            third=lines[2].strip()

            #print(first, second, third)
            set1= set(); set2= set(); set3= set()
            for letter in first:
                set1.add(letter)
            for letter in second:
                set2.add(letter)
            for letter in third:
                set3.add(letter)
            matches = set3.intersection(set1.intersection(set2))
            for letter in matches:
                score += get_priority(letter)

    # return something
    print(score)
    return score 


if __name__ == '__main__':
    process_data()
    process_data2()