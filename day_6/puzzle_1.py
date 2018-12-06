#coding=utf8

import numpy as np
import os
import sys

def manhattan_distance(x, y):
    return sum(abs(x-y))

if __name__ == '__main__':
    input = np.loadtxt("test.txt", dtype=int, delimiter=',')
    area = np.zeros(len(input))
    edge = np.max(input, axis=0)
    infinite = set()
    for i in range(edge[0] + 1):
        for j in range(edge[1] + 1):
            dis = np.array([manhattan_distance([i, j], pair) for pair in input])
            idx = np.where(dis == dis.min())
            if len(idx[0]) != 1:
                continue
            if i == 0 or j == 0 or i == edge[0] or j == edge[1]:
                infinite.add(idx[0][0])
            area[idx[0]] += 1
    for idx in infinite:
        area[idx] = -1
    print max(area)
            
