#coding=utf8

def load_data(filename):
    program = []
    for line in open(filename):
        flist = line.strip().split()
        opt = flist[0]
        step = int(flist[1])
        program.append((opt, step))
    return program

def quiz_one(program):
    accumulator = 0
    idx = 0; visited = set()
    while idx < len(program):
        if idx in visited:
            return accumulator, idx
        visited.add(idx)
        (opt, step) = program[idx]
        if opt == 'acc':
            accumulator += step
            idx += 1
        elif opt == 'nop':
            idx += 1
        elif opt == 'jmp':
            idx += step
    return accumulator, idx

def quiz_two(program):
    for i in range(len(program)):
        (opt, step) = program[i]
        if opt == 'nop':
            new_program = program[:i] + [('jmp', step)] + program[i+1:]
        elif opt == 'jmp':
            new_program = program[:i] + [('nop', step)] + program[i+1:]
        else:
            continue
        accumulator, idx = quiz_one(new_program)
        if idx == len(program):
            return accumulator

if __name__ == '__main__':
    input = load_data('day_8.txt')
    res_1, _ = quiz_one(input)
    print (res_1)
    res_2 = quiz_two(input)
    print (res_2)
