#coding=utf8

import numpy as np
import math

def read_map(filename):
    return [list(line.strip()) for line in open(filename)]

def common_div(x, y):
    x = abs(x); y = abs(y)
    for cd in range(min(x, y), 1, -1):
        if x % cd == 0 and y % cd == 0:
            return cd
    return 1

def get_step(centre, tpoint):
    x = tpoint[0] - centre[0]
    y = tpoint[1] - centre[1]
    cd = common_div(x, y)
    if x == 0:
        step = (0, y / abs(y))
    elif y == 0:
        step = (x / abs(x), 0)
    else:
        step = (x / cd, y / cd)
    return step

def test_one_pair(centre, tpoint, maps):
    step = get_step(centre, tpoint)
    next_x = centre[0]; next_y = centre[1]
    while True:
        next_x += step[0]
        next_y += step[1]
        if next_x == tpoint[0] and next_y == tpoint[1]:
            break
        if maps[next_x][next_y] == '#':
            return False
    return True

def get_station(maps):
    rlen = len(maps)
    clen = len(maps[0])
    counts = [[0] * clen for i in range(rlen)]
    for i in range(rlen):
        for j in range(clen):
            if maps[i][j] != '#':
                continue
            centre = (i, j)
            for t in range(0, rlen):
                for k in range(0, clen):
                    if t == i and j == k:
                        continue
                    if maps[t][k] != '#':
                        continue
                    tpoint = (t, k)
                    if test_one_pair(centre, tpoint, maps):
                        counts[i][j] += 1
    print(np.max(counts))
    counts = np.array(counts)
    return np.unravel_index(counts.argmax(), counts.shape)

def get_degree(c_x, c_y, x, y):
    x = x - c_x
    y = c_y - y
    return math.atan2(x, y) % (2*math.pi)

def get_distance(c_x, c_y, x, y):
    x = x - c_x
    y = y - c_y
    return (x**2 + y**2)**(0.5)

def get_destroy_seq(c_x, c_y, maps):
    rlen = len(maps)
    clen = len(maps[0])
    destroy_dict = {}
    for i in range(rlen):
        for j in range(clen):
            if maps[i][j] != '#':
                continue
            if i == c_y and j == c_x:
                continue
            degree = get_degree(c_x, c_y, j, i)
            distance = get_distance(c_x, c_y, j, i)
            if degree not in destroy_dict:
                destroy_dict[degree] = {}
            destroy_dict[degree][distance] = (j, i)
    return destroy_dict

def sort_destroy_seq(destroy_dict):
    new_destroy = []
    for degree in sorted(destroy_dict.items(), key = lambda d:d[0]):
        degree_dict = degree[1]
        new_list = []
        for distance in sorted(degree_dict.items(), key = lambda d:d[0]):
            new_list.append(distance[1])
        new_destroy.append(new_list)
    return new_destroy

def get_n_destroy(destroy_list, n):
    idx = 0; len_list = len(destroy_list)
    while idx < n:
        for i in range(len_list):
            if len(destroy_list[i]) == 0:
                continue
            (x, y) = destroy_list[i].pop(0)
            idx += 1
            if idx == n:
                return x, y           
    return -1, -1

def part_2(maps, x, y):
    destroy_dict = get_destroy_seq(x, y, maps)
    destroy_list = sort_destroy_seq(destroy_dict)
    n_x, n_y = get_n_destroy(destroy_list, 200)
    print (n_x, n_y)

if __name__ == '__main__':
    maps = read_map('day_10.txt')
    station_y, station_x = get_station(maps)
    print (station_x, station_y)
    part_2(maps, station_x, station_y)
