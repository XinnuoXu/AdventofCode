#coding=utf8
import copy

def decode_command(command):
    opcode = command % 100
    mode_1 = command % 1000 / 100
    mode_2 = command % 10000 / 1000
    mode_3 = command % 100000 / 10000
    return opcode, mode_1, mode_2, mode_3

def get_parameter(mode, parameter, codes):
    # position mode
    if mode == 0:
        return codes[parameter]
    else:
        return parameter

def intCode(raw_codes, input):
    codes = copy.deepcopy(raw_codes)
    idx = 0
    while idx < len(codes):
        opcode, mode_1, mode_2, mode_3 = decode_command(codes[idx])
        if opcode == 99:
            break
        if opcode == 3:
            target = codes[idx+1]
            codes[target] = input
            idx += 2
            continue
        if opcode == 4:
            target = codes[idx+1]
            print (codes[target])
            idx += 2
            continue

        parameter_1 = codes[idx+1]; parameter_2 = codes[idx+2]
        parameter_1 = get_parameter(mode_1, parameter_1, codes)
        parameter_2 = get_parameter(mode_2, parameter_2, codes)
        if opcode == 5:
            idx = parameter_2 if parameter_1 != 0 else idx+3
            continue
        if opcode == 6:
            idx = parameter_2 if parameter_1 == 0 else idx+3
            continue

        target = codes[idx+3]; 
        if opcode == 1:
            codes[target] = parameter_1 + parameter_2          
        elif opcode == 2:
            codes[target] = parameter_1 * parameter_2
        elif opcode == 7:
            codes[target] = 1 if parameter_1 < parameter_2 else 0
        elif opcode == 8:
            codes[target] = 1 if parameter_1 == parameter_2 else 0
        idx += 4
    return 

if __name__ == '__main__':
    with open('day_5.txt') as file:
        codes = file.read().strip().split(',')
    codes = [int(c) for c in codes]
    # part 1
    #intCode(codes, 1)
    # part 2
    intCode(codes, 5)
