#coding=utf8

import sys
import numpy as np

def manhattan_distance(x, y):
    return np.sum(np.absolute(x-y))

def point_to_cluster(p, constellation):
    for c in constellation:
        if manhattan_distance(p, c) <= 3:
            return True
    return False

if __name__ == '__main__':
    points = [np.fromstring(line, dtype=int, sep=",") for line in open("test.txt")]
    constellations = []
    for p in points:
        new_c = []
        new_c.append(p)
        new_constellations = []
        for c in constellations:
            if point_to_cluster(p, c):
                new_c += c
            else:
                new_constellations.append(c)
        new_constellations.append(new_c)
        del constellations[:]
        constellations = new_constellations
    print len(constellations)
