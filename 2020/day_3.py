#coding=utf8

def load_data(filename):
    return [line.strip() for line in open(filename)]

def quiz_one(input, slope):
    (s_right, s_down) = slope
    col_num = len(input[0])
    r = 0; c = 0; tree = 0
    while r < len(input):
        if input[r][c] == '#':
            tree += 1
        r += s_down; c += s_right; c = c%col_num
    return tree

def quiz_two(input, slopes):
    multiply_res = 1
    for slope in slopes:
        tree = quiz_one(input, slope)
        multiply_res *= tree
    return multiply_res

if __name__ == '__main__':
    input = load_data('day_3.txt')

    slope = (3, 1)
    res_1 = quiz_one(input, slope)
    print (res_1)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res_2 = quiz_two(input, slopes)
    print (res_2)
