#coding=utf8

def load_data(filename):
    return [int(line.strip()) for line in open(filename)]

def quiz_one(numbers, preamble):
    sum_queue = []
    preamble_queue = []
    for i in range(preamble):
        num = numbers[i]
        sums = set([numbers[j]+num for j in range(i) if numbers[j] != num])
        sum_queue.append(sums)
        preamble_queue.append(num)
    for i in range(preamble, len(numbers)):
        sums = set().union(*sum_queue)
        if numbers[i] not in sums:
            return numbers[i]
        del sum_queue[0]
        del preamble_queue[0]
        sums = set([numbers[i]+num for num in preamble_queue if numbers[i] != num])
        sum_queue.append(sums)
        preamble_queue.append(numbers[i])
    return -1

def quiz_two(numbers, invalid_num):
    for j in range(0, len(numbers)):
        for i in range(j+2, len(numbers)+1):
            if sum(numbers[j:i]) == invalid_num:
                return min(numbers[j:i]) + max(numbers[j:i])
            elif sum(numbers[j:i]) > invalid_num:
                break
    return -1

if __name__ == '__main__':
    input = load_data('day_9.txt')
    res_1 = quiz_one(input, 25)
    print (res_1)
    res_2 = quiz_two(input, res_1)
    print (res_2)
