#coding=utf8
import copy

def part_1(raw_codes, noun, verb):
    codes = copy.deepcopy(raw_codes)
    codes[1] = noun; codes[2] = verb
    for i in range(0, len(codes), 4):
        command = codes[i]
        target = codes[i+3]
        pos_1 = codes[i+1]; pos_2 = codes[i+2]
        if command == 1:
            codes[target] = codes[pos_1] + codes[pos_2]
        elif command == 2:
            codes[target] = codes[pos_1] * codes[pos_2]
        elif command == 99:
            break
    return codes[0]

def part_2(codes):
    for i in range(0, 100):
        for j in range(0, 100):
            try:
                output = part_1(codes, i, j)
            except:
                continue
            if output == 19690720:
                return i, j
    return -1, -1

if __name__ == '__main__':
    with open('day_2.txt') as file:
        codes = file.read().strip().split(',')
    codes = [int(c) for c in codes] 
    #code_0 = part_1(codes, 12, 2)
    #print (code_0)
    noun, verb = part_2(codes)
    print (100 * noun + verb)