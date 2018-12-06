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
    size = 0
    for i in range(edge[0] + 1):
        for j in range(edge[1] + 1):
            dis = np.array([manhattan_distance([i, j], pair) for pair in input])
            if sum(dis) < 10000:
                size += 1
    print size
            
