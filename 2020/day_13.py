#coding=utf8

def load_data_one(filename):
    with open(filename, 'r') as f:
        output = f.read().strip()
    flist = output.split('\n')
    dep_time = int(flist[0])
    buses = [int(item) for item in flist[1].split(',') if item != 'x']
    return dep_time, buses

def quiz_one(dep_time, buses):
    min_wait_time = dep_time
    min_wait_bus = -1
    for bus in buses:
        wait_time = (int(dep_time/bus)+1)*bus-dep_time
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_wait_bus = bus
    return min_wait_time, min_wait_bus

def load_data_two(filename):
    with open(filename, 'r') as f:
        output = f.read().strip()
    flist = output.split('\n')
    time_gap = 0; rules = []
    for i, item in enumerate(flist[1].split(',')):
        if i == 0:
            target_bus = int(item)
        elif item == 'x':
            time_gap += 1
        else:
            time_gap += 1
            rules.append((target_bus, int(item), time_gap))
    return rules

def min_cands(rule):
    target = rule[0]
    source = rule[1]
    remainds = rule[2]
    lcm = int(np.lcm.reduce([target, source])/target)
    for itt in range(1, lcm):
        if (target * itt + remainds) % source == 0:
            return itt, lcm

def inc_check(rule1, rule2):
    rem_1 = rule1[0]
    loop_1 = rule1[1]
    rem_2 = rule2[0]
    loop_2 = rule2[1]
    itt = 0
    while 1:
        if (loop_1 * itt + rem_1)%loop_2 == rem_2:
            return loop_1 * itt+rem_1, np.lcm.reduce([loop_1, loop_2])
        itt += 1

def quiz_two(rules):
    for i, rule in enumerate(rules):
        itt, lcm = min_cands(rule)
        print (rule, itt, lcm)
        if i == 0:
            rule1 = (itt, lcm)
            continue
        print (rule1)
        print ((itt, lcm))
        rule1 = inc_check(rule1, (itt, lcm))
        print (rule1)
        print ('\n')
    return rule1[0]*rule[0]

if __name__ == '__main__':
    import numpy as np
    dep_time, buses = load_data_one('day_13.txt')
    wait_time, bus = quiz_one(dep_time, buses)
    print (wait_time, bus, wait_time*bus)
    rules = load_data_two('day_13.txt')
    res_2 = quiz_two(rules)
    print (res_2)
