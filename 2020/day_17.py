#coding=utf8

def load_data(filename):
    initial_state = np.zeros((24,24,16), dtype=int)
    x = 8; y = 8; z = 8
    for line in open(filename):
        line = line.strip()
        for i, cube in enumerate(line):
            if cube == '#':
                initial_state[x][y+i][z] = 1
        x += 1
    return initial_state

def quiz_one(initial_state):
    def active_check(state, x, y, z):
        neighbors_state = state[x-1:x+2, y-1:y+2, z-1:z+2].sum()-1
        if neighbors_state in [2, 3]:
            return 1
        return 0
        
    def deactive_check(state, x, y, z):
        neighbors_state = state[x-1:x+2, y-1:y+2, z-1:z+2].sum()
        if neighbors_state == 3:
            return 1
        return 0

    def one_cycle(initial_state):
        updated_state = np.zeros((24,24,16), dtype=int)
        for x in range(1, 23):
            for y in range(1, 23):
                for z in range(1, 15):
                    if initial_state[x][y][z] == 1:
                        updated_state[x][y][z] = active_check(initial_state, x, y, z)
                    if initial_state[x][y][z] == 0:
                        updated_state[x][y][z] = deactive_check(initial_state, x, y, z)
        return updated_state

    for i in range(6):
        initial_state = one_cycle(initial_state)
    return initial_state.sum()


def load_data_two(filename):
    initial_state = np.zeros((24,24,16,16), dtype=int)
    x = 8; y = 8; z = 8; w=8
    for line in open(filename):
        line = line.strip()
        for i, cube in enumerate(line):
            if cube == '#':
                initial_state[x][y+i][z][w] = 1
        x += 1
    return initial_state

def quiz_two(initial_state):
    def active_check(state, x, y, z, w):
        neighbors_state = state[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2].sum()-1
        if neighbors_state in [2, 3]:
            return 1
        return 0
        
    def deactive_check(state, x, y, z, w):
        neighbors_state = state[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2].sum()
        if neighbors_state == 3:
            return 1
        return 0

    def one_cycle(initial_state):
        updated_state = np.zeros((24,24,16, 16), dtype=int)
        for x in range(1, 23):
            for y in range(1, 23):
                for z in range(1, 15):
                    for w in range(1, 15):
                        if initial_state[x][y][z][w] == 1:
                            updated_state[x][y][z][w] = active_check(initial_state, x, y, z, w)
                        if initial_state[x][y][z][w] == 0:
                            updated_state[x][y][z][w] = deactive_check(initial_state, x, y, z, w)
        return updated_state

    for i in range(6):
        initial_state = one_cycle(initial_state)
    return initial_state.sum()

if __name__ == '__main__':
    import numpy as np
    initial_state = load_data('day_17.txt')
    res_1 = quiz_one(initial_state)
    print (res_1)

    initial_state = load_data_two('day_17.txt')
    res_2 = quiz_two(initial_state)
    print (res_2)
