#coding=utf8

def load_data(filename):
    rules = {}
    for line in open(filename):
        line = line.strip().replace('bags', 'bag')[:-1]
        rule = line.split(' contain ')
        if len(rule) != 2:
            continue
        key_bag = rule[0]
        value_bags = rule[1]
        rules[key_bag] = {}
        for item in value_bags.split(', '):
            toks = item.split()
            try:
                bag_num = int(toks[0])
                bag_color = ' '.join(toks[1:])
                rules[key_bag][bag_color] = bag_num
            except:
                pass
    return rules

def reverse_kv(input):
    reversed_rules = {}
    for key in input:
        values = input[key]
        for color in values:
            if color not in reversed_rules:
                reversed_rules[color] = []
            num = values[color]
            reversed_rules[color].append((key, num))
    return reversed_rules

def quiz_one(input, target):
    container_set = set()
    if target not in input:
        return container_set
    for container in input[target]:
        (color, number) = container
        ret_list = quiz_one(input, color)
        container_set.add(color)
        container_set = container_set.union(ret_list)
    return container_set

def quiz_two(input, target):
    if target not in input:
        return 1
    number = 1
    for subbags in input[target]:
        subbags_num = input[target][subbags]
        number += (quiz_two(input, subbags) * subbags_num)
    return number

if __name__ == '__main__':
    input = load_data('day_7.txt')
    res_1 = quiz_one(reverse_kv(input), 'shiny gold bag')
    print (len(res_1))
    res_2 = quiz_two(input, 'shiny gold bag')
    print (res_2-1)
