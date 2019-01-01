#coding=utf8

import re
import numpy as np

def manhattan_distance(x, y):
    return np.sum(np.absolute(x-y))

if __name__ == '__main__':
    inputs = [line.strip().replace("pos=<", "").replace(">, r=", ",") for line in open("test.txt")]
    nanobots = np.array([np.fromstring(line, dtype=int, sep=",").tolist() for line in inputs])
    largest_nano = np.argmax(nanobots[:, -1])
    in_range = 0
    for bot in nanobots:
        if manhattan_distance(bot[:-1], nanobots[largest_nano][:-1]) <= nanobots[largest_nano][-1]:
            in_range += 1
    print in_range
