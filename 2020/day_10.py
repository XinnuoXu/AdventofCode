#coding=utf8

def load_data(filename):
    adapters = [int(line.strip()) for line in open(filename)]
    adapters.sort()
    return [0] + adapters + [adapters[-1]+3]

def quiz_one(adapters):
    diff = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
    return diff.count(1) * diff.count(3)

def quiz_two(adapters):
    diff = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]
    solutions = 1
    accum = 0
    mapping = {2:2, 3:4, 4:7}
    for item in diff:
        if item == 1:
            accum += 1
        else:
            if accum in mapping:
                solutions *= mapping[accum]
            accum = 0
    return solutions

if __name__ == '__main__':
    input = load_data('day_10.txt')
    res_1 = quiz_one(input)
    print (res_1)
    res_2 = quiz_two(input)
    print (res_2)
