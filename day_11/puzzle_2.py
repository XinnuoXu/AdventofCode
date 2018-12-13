#coding=utf8

import numpy as np
serial = 42
x_axis = 300
y_axis = 300

def mask_n(grid, n):
    max_sum = 0; max_x = -1; max_y = -1
    for x in range(x_axis):
        for y in range(y_axis):
            if x >=n and y >= n:
                square = grid[x-n:x+1, y-n:y+1]
                if np.sum(square) > max_sum:
                    max_sum = np.sum(square)
                    max_x = x-n
                    max_y = y-n
    return max_x + 1, max_y + 1, max_sum

if __name__ == '__main__':
    grid = np.zeros([x_axis, y_axis])
    for x in range(x_axis):
        for y in range(y_axis):
            rack_id = x + 1 + 10
            power = rack_id * (y + 1)
            power = power + serial
            power = power * rack_id
            power = power / 100 - (power / 1000) * 10
            power = power - 5
            grid[x][y] = power

    max_sum = 0; max_x = -1; max_y = -1; max_n = 0
    for i in range(1, 300):
        x, y, ssum = mask_n(grid, i)
        if ssum > max_sum:
            max_sum = ssum;
            max_x = x;
            max_y = y;
            max_n = i + 1
    print max_x, max_y, max_n
