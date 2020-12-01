#coding=utf8

def load_data(filename):
    return [int(line.strip()) for line in open(filename)]

def quiz_one(input, target):
    rest = set()
    for item in input:
        if item in rest:
            return item * (target-item)
        rest.add(target-item)
    return -1

def quiz_two(input, target):
    for i in range(len(input)):
        ret = quiz_one(input[:i] + input[(i+1):], target-input[i])
        if ret != -1:
            return ret * input[i]

if __name__ == '__main__':
    input = load_data('day_1.txt')
    res_1 = quiz_one(input, 2020)
    res_2 = quiz_two(input, 2020)
    print (res_2)
