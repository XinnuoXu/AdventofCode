#coding=utf8

def read_orbit(filename):
    orbits = {}
    for line in open(filename):
        flist = line.strip().split(')')
        left = flist[0]
        right = flist[1]
        if left not in orbits:
            orbits[left] = []
        orbits[left].append(right)
    return orbits

def part_1(orbits):
    core_stack = ['COM']
    orbits_stack = [0]
    orbit_num = 0
    while len(core_stack) > 0:
        core = core_stack.pop()
        core_orbits_num = orbits_stack.pop()
        orbit_num += core_orbits_num
        if core not in orbits:
            continue
        core_stack.extend(orbits[core])
        orbits_stack.extend([core_orbits_num+1] * len(orbits[core]))
    print (orbit_num)

def read_reverse_orbit(filename):
    orbits = {}
    for line in open(filename):
        flist = line.strip().split(')')
        left = flist[0]
        right = flist[1]
        orbits[right] = left
    return orbits

def part_2(orbits, rev_orbits):
    you_path = []; santa_path = []
    core = 'YOU'
    while core != 'COM':
        core = rev_orbits[core]
        you_path.append(core)
    core = 'SAN'
    while core != 'COM':
        core = rev_orbits[core]
        santa_path.append(core)
    distance = len(you_path) + len(santa_path)
    for i in range(len(you_path)):
        for j in range(len(santa_path)):
            if you_path[i] == santa_path[j] and i + j < distance:
                distance = i + j
    print (distance)

if __name__ == '__main__':
    #orbits = read_orbit('day_6.txt')
    #part_1(orbits)
    rev_orbits = read_reverse_orbit('day_6.txt')
    orbits = read_orbit('day_6.txt')
    part_2(orbits, rev_orbits)