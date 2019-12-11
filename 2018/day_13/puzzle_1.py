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
    # move
    if cart[2] == 'v':
        cart[0] += 1 
    elif cart[2] == '^':
        cart[0] -= 1 
    elif cart[2] == '>':
        cart[1] += 1
    elif cart[2] == '<':
        cart[1] -= 1
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
    return [x, y, direction, turn_count]

def collision(carts):
    tmp_dict = set()
    for cart in carts:
        if str(cart[0]) + " " + str(cart[1]) in tmp_dict:
            print cart[1], cart[0]
            return True
        tmp_dict.add(str(cart[0]) + " " + str(cart[1]))
    return False

if __name__ == '__main__':
    data = [list(line.strip("\r\n")) for line in open("test.txt")]
    maze, carts = maze_and_carts(data)
    while not collision(carts):
        for i in range(len(carts)):
            carts[i] = one_move(maze, carts[i])
