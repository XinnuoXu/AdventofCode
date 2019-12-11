#coding=utf8

import numpy as np
serial = 3999
x_axis = 300
y_axis = 300

if __name__ == '__main__':
    grid = np.zeros([x_axis, y_axis])
    max_sum = 0; max_x = -1; max_y = -1
    for x in range(x_axis):
        for y in range(y_axis):
            rack_id = x + 1 + 10
            power = rack_id * (y + 1)
            power = power + serial
            power = power * rack_id
            power = power / 100 - (power / 1000) * 10
            power = power - 5
            grid[x][y] = power
            if x >=2 and y >= 2:
                square = grid[x-2:x+1, y-2:y+1]
                if np.sum(square) > max_sum:
                    max_sum = np.sum(square)
                    max_x = x-2
                    max_y = y-2
    print max_x + 1, max_y + 1
