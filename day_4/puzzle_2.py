#coding=utf8

if __name__ == '__main__':
    import re
    import sys
    import os
    import operator
    import numpy as np
    os.system("sort -k1 test.txt > tmp")
    entries = [line.strip().replace("falls asleep", "10000").replace("wakes up", "20000") for line in open("tmp")]
    entries = map(lambda s: map(int, re.findall(r'\d+', s)), entries)
    sleep_time = -1
    id = -1
    ent_dict = {}
    for ent in entries:
        if ent[-1] < 10000:
            #make record
            if sleep_time > -1:
                for i in range(sleep_time, 60):
                    one_day[i] = 1
            if id > -1:
                if id not in ent_dict:
                    ent_dict[id] = []
                ent_dict[id].append(one_day)
            #refresh
            id = ent[-1]
            one_day = np.zeros(60)
            sleep_time = -1
        elif ent[-1] == 10000:
            sleep_time = ent[-2]
        elif ent[-1] == 20000:
            wake_time = ent[-2]
            for i in range(sleep_time, wake_time):
                one_day[i] = 1
            sleep_time = -1
    if sleep_time > -1:
        for i in range(sleep_time, 60):
            one_day[i] = 1
    if id not in ent_dict:
        ent_dict[id] = []
    ent_dict[id].append(one_day)

    max_sleep_time_dict = {}
    max_id = -1; max_times = -1
    for id in ent_dict:
        ent = np.concatenate(ent_dict[id], axis=0).reshape(len(ent_dict[id]), -1)
        max_sleep_time_dict[id] = np.argmax(np.sum(ent, axis=0))
        times = np.max(np.sum(ent, axis=0))
        if times > max_times:
            max_times = times; max_id = id
    print max_times, max_id, max_sleep_time_dict[max_id], max_id * max_sleep_time_dict[max_id]
