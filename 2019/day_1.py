#coding=utf8

def fuel(mass):
    return mass / 3 - 2

def recurrent_fuel(mass):
    fuel_sum = 0.0
    while mass > 6:
        mass = mass / 3 - 2
        fuel_sum += mass
    return fuel_sum

def part_1():
    print (sum([fuel(int(line.strip())) for line in open("day_1.txt")]))

def part_2():
    print (sum([recurrent_fuel(int(line.strip())) for line in open("day_1.txt")]))

if __name__ == '__main__':
    part_2()