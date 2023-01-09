import math
import os
import numpy as np
import time
import scipy.sparse as sparse
class Diamond():
    def __init__(self, xs,ys,distance, mat_size):
        self.xs = xs
        self.ys = ys
        self.corners = {"right":(xs+distance, ys), "left":(xs-distance, ys), "top":(xs, ys+distance), "bottom": (xs, ys-distance)}
        self.top_edges = set()
        self.bottom_edges = set()
        self.distance = distance
        self.mat_size = mat_size
        for x in range(max([0,self.corners["left"][0]]),min([self.corners["right"][0], mat_size])):
            yb, yt = ys-(distance-x), ys+(distance-x)
            if yt >= 0 and yt < self.mat_size:
                self.top_edges.add((x,yt))
            if yb >= 0 and yb < self.mat_size:
                self.bottom_edges.add((x,yb))
    def contain(self,x,y):
        if abs(x-self.xs)+abs(y-self.ys) <= self.distance:
                return True
        return False



def process_data():
    # read data
    with open('inputs/aoc15.txt') as data:
        lines = [line.rstrip("\n").rsplit(" ") for line in data]
    # variables
    find_y = 2000000
    mat_size = 4000000
    score = 0
    # (sensor):(closest beacon)
    sensors= {}
    # process lines.
    for line in lines:
        sensors[(int(line[2][2:-1]),int(line[3][2:-1]))]=(int(line[8][2:-1]),int(line[9][2:]))
    #print(sensors)

    no_beacon = set()
    diamonds = []
    no = 0
    for sensor in sensors:
        no += 1
        xs,ys = sensor[0], sensor[1]
        xb,yb = sensors[sensor][0], sensors[sensor][1]
        dx = abs(xs-xb)
        dy = abs(ys-yb)
        dist = dx+dy
        diamond = Diamond(xs,ys,dist, mat_size)
        diamonds.append(diamond)
        print(f"diamond {no}., {diamond}")
    print("--- adding diamonds %s seconds ---" % (time.time() - start_time))
    ######## Part 1 ##
        # if find_y >= ys-dist and find_y <= ys+dist+1:
        #     for i in range(xs-dist,xs+dist+1):
        #         for j in [find_y]:
        #             #print(i,j)
        #             di = abs(xs-i)
        #             dj = abs(ys-j)
        #             idist = di+dj
        #             if idist <= dist:
        #                 no_beacon.add((i,j))
        #                 #print(i,j)
        
    #print(no_beacon)
    #remove positions with beacons already.

    # for sensor in sensors:
    #     beacon = sensors[sensor]
    #     #print(beacon)
    #     if beacon in no_beacon:
    #         print(f"removed beacon {beacon}")
    #         no_beacon.discard(beacon)
    ################
    # matrix = [""]*20# np.zeros((20,20), dtype=str)
    # printpos = set()
    # for item in diamonds:
    #     for pos in item.top_edges:
    #         printpos.add(pos)
    #     for pos in item.bottom_edges:
    #         printpos.add(pos)
    # for x in range(20):
    #     for y in range(20):
    #         if (x,y) in printpos:
    #             matrix[x] += "#"
    #         else:
    #             matrix[x] += "."
    # for line in matrix:
    #     print(line)
    # plot = []
    # for x in matrix:
    #     for y in x:



    n = len(no_beacon)
    print(f"answer part 1: {n}")


    # TODO: check all diamond.top_edge(x,y+1) and diamond.bottom_edge(x,y-1)
    #       and diamond.corners["left"](x-1,y) and diamond.corners["right"](x+1,y).     
    for diamond in diamonds:
        for pos in diamond.top_edges:
            n = 0
            for idiamond in diamonds:
                if idiamond.contain(pos[0], pos[1]+1):
                    n += 1
            if n == 0:
                print(pos)
        for pos in diamond.bottom_edges:
            n = 0
            for idiamond in diamonds:
                if idiamond.contain(pos[0], pos[1]+1):
                    n += 1
            if n == 0:
                print(pos)
        n = 0
        for idiamond in diamonds:
            if idiamond.contain(diamond.corners["left"][0]-1, diamond.corners["left"][0]):
                n += 1
        if n == 0:
            print("left")
            print(diamond.corners["left"])
        n = 0
        for diamond in diamonds:
            if idiamond.contain(diamond.corners["right"][0]+1, diamond.corners["right"][0]):
                n += 1
        if n == 0:
            print("right")
            print(diamond.corners["right"])






    #return something
    print(score)
    return score


if __name__ == '__main__':
    start_time = time.time()
    process_data()
    print("--- End %s seconds ---" % (time.time() - start_time))
    