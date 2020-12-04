#coding=utf8

import os, sys
import re

def load_data(filename):
    passports = []; kvs = {}
    for line in open(filename):
        line = line.strip()
        if len(line) == 0:
            passports.append(kvs)
            kvs = {}
            continue
        for kv in line.split():
            kv = kv.split(':')
            key = kv[0]
            value = kv[1]
            kvs[key] = value
    if len(kvs) > 0:
        passports.append(kvs)
    return passports

def key_check(passport, optional='', full_knum=8):
    if len(passport) == full_knum:
        return True
    if (len(passport) == full_knum-1) and (optional not in passport):
        return True
    return False

def year_check(yr, mi=0, ma=0):
    try:
        yr = int(yr)
    except:
        return False
    if yr <= ma and yr >= mi:
        return True
    return False

def hight_check(hgt):
    rules = {'cm':(150, 193), 'in':(59, 76)}
    if len(hgt) < 3:
        return False
    if hgt[-2:] not in rules:
        return False
    try:
        num = int(hgt[:-2])
    except:
        return False
    (mi, ma) = rules[hgt[-2:]]
    if num >= mi and num <= ma:
        return True
    return False

def eye_check(ecl):
    if ecl in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return True
    return False

def hair_check(hcl):
    pattern = '^#[a-f0-9]{6}$'
    if re.match(pattern, hcl, flags=0) is None:
        return False
    return True
    
def pid_check(pid):
    pattern = '^[0-9]{9}$'
    if re.match(pattern, pid, flags=0) is None:
        return False
    return True
    
def value_check(passport):

    byr = passport['byr']
    if not year_check(byr, mi=1920, ma=2002):
        return False

    iyr = passport['iyr']
    if not year_check(iyr, mi=2010, ma=2020):
        return False

    eyr = passport['eyr']
    if not year_check(eyr, mi=2020, ma=2030):
        return False

    hgt = passport['hgt']
    if not hight_check(hgt):
        return False

    hcl = passport['hcl']
    if not hair_check(hcl):
        return False

    ecl = passport['ecl']
    if not eye_check(ecl):
        return False

    pid = passport['pid']
    if not pid_check(pid):
        return False

    return True

def quiz_one(passports, optional='', full_knum=8):
    valid = 0
    for passport in passports:
        if key_check(passport, optional=optional, full_knum=full_knum):
            valid += 1
    return valid

def quiz_two(passports, optional='', full_knum=8):
    valid = 0
    for passport in passports:
        if not key_check(passport, optional=optional, full_knum=full_knum):
            continue
        if value_check(passport):
            valid += 1
    return valid

if __name__ == '__main__':
    passports = load_data('day_4.txt')
    res_1 = quiz_one(passports, optional='cid', full_knum=8)
    print (res_1)
    res_2 = quiz_two(passports, optional='cid', full_knum=8)
    print (res_2)
