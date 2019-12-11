#coding=utf8

import os
import sys

def react_detection(x, y):
    if x.lower() == y.lower() and x.islower() != y.islower():
        return True
    else:
        return False

if __name__ == '__main__':
    input = open("test.txt").readline().strip()
    remain_units = []
    start_pos = 0
    idx = 0
    while idx + 1 < len(input):
        if not react_detection(input[idx], input[idx+1]):
            idx += 1
            continue
        remain_units.append([start_pos, idx])
        #while idx + 1 < len(input) and react_detection(input[idx], input[idx+1]):
        #    idx += 1
        idx += 2
        while len(remain_units):
            remains = remain_units.pop()
            r_idx = remains[1] - 1
            while r_idx >= remains[0] and idx < len(input):
                if not react_detection(input[r_idx], input[idx]):
                    break
                else:
                    idx += 1
                    r_idx -= 1
            if r_idx < remains[0]:
                continue
            else:
                remain_units.append([remains[0], r_idx+1])
                break
        start_pos = idx
    remain_units.append([start_pos, len(input)])
    sum = 0
    for item in remain_units:
        sum += (item[1] - item[0])
    print sum
