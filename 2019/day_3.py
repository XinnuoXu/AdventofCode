#coding=utf8
import sys

def add_one_step(wire, x, y, direction, step_len, sum_steps):
    if direction == 'R':
        for i in range(x + 1, x + step_len + 1):
            wire['X' + str(i) + 'Y' + str(y)] = (i, y, sum_steps + i - x)
        x = x + step_len
    elif direction == 'U':
        for i in range(y + 1, y + step_len + 1):
            wire['X' + str(x) + 'Y' + str(i)] = (x, i, sum_steps + i - y)
        y = y + step_len
    elif direction == 'L':
        for i in range(x - 1, x - step_len - 1, -1):
            wire['X' + str(i) + 'Y' + str(y)] = (i, y, sum_steps + x - i)
        x = x - step_len
    elif direction == 'D':
        for i in range(y - 1, y - step_len - 1, -1):
            wire['X' + str(x) + 'Y' + str(i)] = (x, i, sum_steps + y - i)
        y = y - step_len
    sum_steps += step_len
    return wire, x, y, sum_steps

def load_wire(data):
    x = 0; y = 0; wire = {}; sum_steps = 0
    for step in data:
        direction = step[0]
        step_len = int(step[1:])
        wire, x, y, sum_steps = add_one_step(wire, x, y, direction, step_len, sum_steps)
    return wire

def load_data(filename):
    wires = []
    for line in open(filename):
        wire = load_wire(line.strip().split(","))
        wires.append(wire)
    return wires

def get_cross(wire1, wire2):
    min_dis = 100000
    for item in wire2:
        if item not in wire1:
            continue
        if abs(wire1[item][0]) + abs(wire1[item][1]) < min_dis:
            min_dis = abs(wire1[item][0]) + abs(wire1[item][1])
    return min_dis

def get_first_cross(wire1, wire2):
    min_step = 100000
    for item in wire2:
        if item not in wire1:
            continue
        if wire1[item][2] + wire2[item][2] < min_step:
            min_step = wire1[item][2] + wire2[item][2]
    return min_step

def part1(filename):
    wires = load_data(filename)
    min_dis = get_cross(wires[0], wires[1])
    print (min_dis)

def part2(filename):
    wires = load_data(filename)
    min_dis = get_first_cross(wires[0], wires[1])
    print (min_dis)

if __name__ == '__main__':
    #part1('day_3.txt')
    part2('day_3.txt')