import math
import os
try:
   from itertools import izip_longest
except ImportError:  # Python 3
    from itertools import zip_longest as izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def get_overlap(sects):
    
    sections = []
    for item in sects:
        sect_range = item.split("-")
        
        start = int(sect_range[0])
        end = int(sect_range[1])
        sections.append(range(start, end+1))
    #overlap = set(sections[0]).intersection(sections[1])
    overlap = [x for x in sections[0] if x in sections[1]]
    print(sects)
    print(overlap)
    if overlap:
        return True
        



def process_line(line):
    sects = line.split(",")
    if get_overlap(sects):
        return True


def process_data():
    filename = 'inputs/aoc4.txt'

    # variables
    score = 0
    
    # read N lines from file
    N = 1
    with open(filename) as f:
        for lines in grouper(f, N, ''):
            assert len(lines) == N
            line = lines[0].strip()
            #print(line)
            if process_line(line):
                score += 1

            


    # return something
    print(score)
    return score 


if __name__ == '__main__':
    process_data()