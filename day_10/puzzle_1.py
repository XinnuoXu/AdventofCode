#coding=utf8

import re
import numpy as np
np.set_printoptions(threshold=np.nan)

if __name__ == '__main__':
    points = [line.strip() for line in open("test.txt")]
    points = map(lambda s: map(int, re.findall(r'-?\d+', s)), points)
    points = np.array(points)
    step = 0
    while 1:
        max_edge = np.amax(points, axis=0)
        min_edge = np.amin(points, axis=0)
        left_top = [min_edge[0], max_edge[1]]
        left_bottom = [min_edge[0], min_edge[1]]
        right_top = [max_edge[0], max_edge[1]]
        right_bottom = [max_edge[0], min_edge[1]]
        positions = points[:, :2].tolist()
        if (left_top in positions and right_top in positions) \
            or (left_bottom in positions and right_bottom in positions):
                break
        step += 1
        for point in points:
            point[0] += point[2]
            point[1] += point[3]
    num_col = max_edge[0] - min_edge[0] + 1
    num_row = max_edge[1] - min_edge[1] + 1
    matrix = np.zeros([num_row, num_col], dtype=int)
    x_tune = min_edge[0]
    y_tune = min_edge[1]
    for point in points:
        point[0] -= x_tune
        point[1] -= y_tune
        matrix[point[1]][point[0]] = 1
    print np.array2string(matrix, separator='').replace("[", "").replace("]", "").replace("0", ".").replace("1", "#")
    print step
