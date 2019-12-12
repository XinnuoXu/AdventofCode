#coding=utf8

def part_1(input, wide, tall):
    min_0 = len(input); output = 0
    for i in range(0, len(input), wide * tall):
        layer = input[i: i + wide * tall]
        num_0 = layer.count('0')
        num_1 = layer.count('1')
        num_2 = layer.count('2')
        if num_0 < min_0:
            min_0 = num_0
            output = num_1 * num_2
    return output

def part_2(input, wide, tall):
    output = [2] * (wide * tall)
    for i in range(0, len(input), wide * tall):
        layer = input[i: i + wide * tall]
        for j in range(len(output)):
            if output[j] in ['0', '1']:
                continue
            if layer[j] in ['0', '1']:
                output[j] = layer[j]
    for i in range(0, len(output), wide):
        print (''.join(output[i: i+wide]).replace('1', '*').replace('0', ' '))
    return output

if __name__ == '__main__':
    with open('day_8.txt') as file:
        input = file.read().strip()
    wide = 25; tall = 6
    #print (part_1(input, wide, tall))
    part_2(input, wide, tall)