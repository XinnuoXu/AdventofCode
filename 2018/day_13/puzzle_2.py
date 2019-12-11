#coding=utf8

import sys

# "left", "straight", "right"
turning = {'^':['<', '^', '>'], \
'>':['^', '>', 'v'], \
'v':['>', 'v', '<'], \
'<':['v', '<', '^']}

def maze_and_carts(data):
    # x, y, direction, intersections moves "left", "straight", "right"
    carts = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'v':
                data[i][j] = '|'
                carts.append([i, j, 'v', 0])
            elif data[i][j] == '^':
                data[i][j] = '|'
                carts.append([i, j, '^', 0])
            elif data[i][j] == '<':
                data[i][j] = '-'
                carts.append([i, j, '<', 0])
            elif data[i][j] == '>':
                data[i][j] = '-'
                carts.append([i, j, '>', 0])
    return data, carts

def one_move(maze, cart):
    x = cart[0]; y = cart[1]; direction = cart[2]; turn_count = cart[3]
    # turn or not
    if maze[x][y] == '+':
        direction = turning[direction][turn_count%3]
        turn_count += 1
    elif maze[x][y] == '/': 
        if direction == '^':
            direction = turning[direction][2]
        elif direction == '>':
            direction = turning[direction][0]
        elif direction == '<':
            direction = turning[direction][0]
        elif direction == 'v':
            direction = turning[direction][2]
    elif maze[x][y] == '\\': 
        if direction == '^':
            direction = turning[direction][0]
        elif direction == '>':
            direction = turning[direction][2]
        elif direction == '<':
            direction = turning[direction][2]
        elif direction == 'v':
            direction = turning[direction][0]
    # move
    if direction == 'v':
        x += 1 
    elif direction == '^':
        x -= 1 
    elif direction == '>':
        y += 1
    elif direction == '<':
        y -= 1
    return [x, y, direction, turn_count]

def collision(carts, i):
    remains = 0
    collision = 0
    for j in range(len(carts)):
        if j == i:
            continue
        if carts[j][0] == -1:
            continue
        if carts[j][0] == carts[i][0] and carts[j][1] == carts[i][1]:
            carts[j][0] = -1
            collision += 1
            continue
        remains += 1
    if collision > 0:
        carts[i][0] = -1
    else:
        remains += 1
    return carts, remains

if __name__ == '__main__':
    data = [list(line.strip("\r\n")) for line in open("test.txt")]
    maze, carts = maze_and_carts(data)
    remains = len(carts)
    while 1:
        for i in range(len(carts)):
            if carts[i][0] == -1:
                continue
            carts[i] = one_move(maze, carts[i])
            carts, remains = collision(carts, i)
        if remains == 1:
            break
    for i in range(len(carts)):
        if carts[i][0] != -1:
            print carts[i][1], carts[i][0]
