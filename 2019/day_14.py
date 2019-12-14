#coding=utf8
import sys

def load(filename):
    reactions = {}
    for line in open(filename):
        flist = line.strip().split(' => ')
        reaction_res = flist[1].split(' ')
        reaction_res_num = int(reaction_res[0])
        reaction_res_ele = reaction_res[1]
        ingredients = []
        for ing in flist[0].split(', '):
            ing_list = ing.split(' ')
            ingredients.append((int(ing_list[0]), ing_list[1]))
        reactions[reaction_res_ele] = (reaction_res_num, ingredients)
    return reactions

def update_stocks(required_num, stocks, ele):
    if required_num < stocks[ele]:
        stocks[ele] -= required_num
        return 0, stocks
    else:
        required_num -= stocks[ele]
        stocks[ele] = 0
        return required_num, stocks
    
def get_reaction_num(required_num, generated_num):
    if required_num % generated_num == 0:
        return required_num / generated_num, 0
    else:
        reaction_num = required_num / generated_num + 1
        left_over = reaction_num * generated_num - required_num
        return reaction_num, left_over

def get_ore(required_num, reactions, ores, stocks, cur_ele):
    if cur_ele == 'ORE':
        return ores+required_num, stocks

    cur_reaction = reactions[cur_ele]
    required_num, stocks = update_stocks(required_num, stocks, cur_ele)
    if required_num == 0:
        return ores, stocks

    generated_num = cur_reaction[0]
    reaction_num, left_over = get_reaction_num(required_num, generated_num)
    stocks[cur_ele] = left_over

    required_reaction = cur_reaction[1]
    for rea in required_reaction:
        re_num = rea[0]
        re_ele = rea[1]
        ores, stocks = get_ore(re_num * reaction_num, reactions, ores, stocks, re_ele)
    return ores, stocks

def part_1(filename):
    reactions = load(filename)
    stocks = {}
    for ele in reactions:
        stocks[ele] = 0
    ores, stocks = get_ore(1, reactions, 0, stocks, 'FUEL')

def part_2(filename):
    cargo_holds = 1000000000000
    reactions = load(filename)
    stocks = {}
    for ele in reactions:
        stocks[ele] = 0
    ores = 0; fuel_num = 0
    while ores <= cargo_holds:
        cost, stocks = get_ore(1, reactions, 0, stocks, 'FUEL')
        ores += cost
        fuel_num += 1
    print (fuel_num-1)

if __name__ == '__main__':
    #part_1("day_14.txt")
    part_2("day_14.txt")
