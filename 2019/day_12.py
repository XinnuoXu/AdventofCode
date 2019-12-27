#coding=utf8
import copy

def read(filename):
    moons = []
    for line in open(filename):
        moon = [int(item[2:]) for item in line.strip()[1:-1].split(', ')]
        moons.append(moon)
    return moons

def read_col(filename):
    moons = [[], [], []]
    for line in open(filename):
        for i, pos in enumerate([int(item[2:]) for item in line.strip()[1:-1].split(', ')]):
            moons[i].append(pos)
    return moons

def update_vel_pair(moon1_pos, moon2_pos, moon1_vel, moon2_vel):
    if moon1_pos > moon2_pos:
        moon1_vel -= 1
        moon2_vel += 1
    elif moon1_pos < moon2_pos:
        moon1_vel += 1
        moon2_vel -= 1
    return moon1_vel, moon2_vel

def update_pos_each(moon_pos, moon_vel):
    moon_pos += moon_vel
    return moon_pos

def update_vel(moons_pos, moons_vel):
    for i in range(len(moons_pos)):
        for j in range(i+1, len(moons_pos)):
            moons_vel[i], moons_vel[j] = update_vel_pair(moons_pos[i], moons_pos[j], moons_vel[i], moons_vel[j])
    return moons_vel

def update_pos(moons_pos, moons_vel):
    for i in range(len(moons_pos)):
        moons_pos[i] = update_pos_each(moons_pos[i], moons_vel[i])
    return moons_pos

def energy_each(moon_pos, moon_vel, dim):
    pos_energy = 0
    vel_energy = 0
    for i in range(len(moon_pos)):
        pos_energy += abs(moon_pos[i], dim)
        vel_energy += abs(moon_vel[i], dim)
    return pos_energy * vel_energy

def get_energy(moons_pos, moons_vel):
    return sum([energy_each(moons_pos[i], moons_vel[i]) for i in range(len(moons_pos))])

def judge_speed(vels):
    for item in vels:
        if item != 0:
            return True
    return False

def lcm(steps):
    lcm = 1
    for s in steps:
        lcm *= s
    return lcm / gcd(steps)

def gcd(steps):
    min_s = min(steps)
    gcd = 1
    for g in range(1, min_s+1):
        is_gcd = True
        for s in steps:
            if s % g != 0:
                is_gcd = False
                break
        if is_gcd:
            gcd = g
    return gcd
        
if __name__ == '__main__':
    #moons_pos = read('day_12.txt')
    moons_pos = read_col('day_12.txt')
    converge_steps = []
    for dim in range(3):
        step = 0
        moons_vel = [0] * len(moons_pos[dim])
        #print ('************\n\n')
        #print (moons_pos[dim])
        #print (moons_vel)
        while step == 0 or judge_speed(moons_vel):
            moons_vel = update_vel(moons_pos[dim], moons_vel)
            moons_pos[dim] = update_pos(moons_pos[dim], moons_vel)
            #print(moons_vel)
            step += 1
        converge_steps.append(step)
    #print (get_energy(moons_pos, moons_vel))
    print (lcm(converge_steps))
    
    