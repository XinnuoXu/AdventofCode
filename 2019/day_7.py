#coding=utf8
import copy

class IntCode():
    def __init__(self, raw_codes):
        self.codes = copy.deepcopy(raw_codes)
        self.idx = 0
        self.stop = False
        self.output = None

    def decode_command(self, command):
        opcode = command % 100
        mode_1 = command % 1000 / 100
        mode_2 = command % 10000 / 1000
        mode_3 = command % 100000 / 10000
        return opcode, mode_1, mode_2, mode_3

    def get_parameter(self, mode, parameter, codes):
        # position mode
        if mode == 0:
            return codes[parameter]
        else:
            return parameter

    def run(self, inputs):
        input_idx = 0
        while self.idx < len(self.codes):
            opcode, mode_1, mode_2, mode_3 = self.decode_command(self.codes[self.idx])
            if opcode == 99:
                self.stop = True
                return
            if opcode == 3:
                target = self.codes[self.idx+1]
                self.codes[target] = inputs[min(len(inputs)-1, input_idx)]
                self.idx += 2
                input_idx += 1
                continue
            if opcode == 4:
                target = self.codes[self.idx+1]
                self.output = self.codes[target]
                self.idx += 2
                return

            parameter_1 = self.codes[self.idx+1]; parameter_2 = self.codes[self.idx+2]
            parameter_1 = self.get_parameter(mode_1, parameter_1, self.codes)
            parameter_2 = self.get_parameter(mode_2, parameter_2, self.codes)
            if opcode == 5:
                self.idx = parameter_2 if parameter_1 != 0 else self.idx+3
                continue
            if opcode == 6:
                self.idx = parameter_2 if parameter_1 == 0 else self.idx+3
                continue

            target = self.codes[self.idx+3]; 
            if opcode == 1:
                self.codes[target] = parameter_1 + parameter_2          
            elif opcode == 2:
                self.codes[target] = parameter_1 * parameter_2
            elif opcode == 7:
                self.codes[target] = 1 if parameter_1 < parameter_2 else 0
            elif opcode == 8:
                self.codes[target] = 1 if parameter_1 == parameter_2 else 0
            self.idx += 4

def get_combinition(b, e):
    return [(a, c, d, f, g) for a in range(b,e) for c in range(b,e) for d in range(b,e) for f in range(b,e) for g in range(b,e)]

def part_1(codes):
    max_score = 0
    for comb in get_combinition(0, 5):
        if len(set(comb)) < 5:
            continue
        amplifiers = [IntCode(codes) for i in range(5)]
        for i, instruction in enumerate(comb):
            if i == 0:
                last_output = 0
            last_output = amplifiers[i].run([instruction, last_output])
        if last_output > max_score:
            max_score = last_output
    print (max_score)

def part_2(codes):
    max_score = 0
    for comb in get_combinition(5, 10):
        if len(set(comb)) < 5:
            continue
        amplifiers = [IntCode(codes) for i in range(5)]
        loop_idx = 0; last_output = 0; last_e_output = 0;
        while True:
            idx = loop_idx % 5
            if loop_idx / 5 == 0:
                amplifiers[idx].run([comb[idx], last_output])
            else:
                amplifiers[idx].run([last_output])
            last_output = amplifiers[idx].output
            if idx == 4:
                last_e_output = last_output
            if amplifiers[idx].stop:
                break
            loop_idx += 1
        if last_e_output > max_score:
            max_score = last_e_output
    print (max_score)

if __name__ == '__main__':
    with open('day_7.txt') as file:
        codes = file.read().strip().split(',')
    codes = [int(c) for c in codes]
    #part_1(codes)
    part_2(codes)
