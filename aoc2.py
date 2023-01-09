import math
import os


def process_data():
    data = open('inputs/aoc2.txt', 'r')
    lines = data.readlines()

    # variables
    score = 0
    score_table = {"A X":3, "A Y":4 , "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7}
    # extract data from file
    for item in lines:
      
        #print(score_table["A X"])
        score += score_table[item.strip()]


    # return something
    print(score)
    return score 


if __name__ == '__main__':
    process_data()