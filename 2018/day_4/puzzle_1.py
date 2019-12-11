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
    sleep_time_dict = {}
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
                if id not in sleep_time_dict:
                    sleep_time_dict[id] = 0
                sleep_time_dict[id] += sum(one_day)
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
    if id not in sleep_time_dict:
        sleep_time_dict[id] = 0
    sleep_time_dict[id] += sum(one_day)

    max_id = max(sleep_time_dict.iteritems(), key=operator.itemgetter(1))[0]
    max_ent = np.concatenate(ent_dict[max_id], axis=0).reshape(len(ent_dict[max_id]), -1)
    print max_id * np.argmax(np.sum(max_ent, axis=0))
