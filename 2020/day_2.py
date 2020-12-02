#coding=utf8

class OneLine():
    def __init__(self, line):
        mi, ma, tar, string = self.read(line)
        self.mi = mi
        self.ma = ma
        self.tar = tar
        self.string = string

    def read(self, line):
        line = line.strip()
        flist = line.split()
        ms = flist[0].split('-')
        mi = int(ms[0])
        ma = int(ms[1])
        tar = flist[1][:-1]
        string = flist[2]
        return mi, ma, tar, string

    def check_one(self):
        di = {}
        for s in self.string:
            if s not in di:
                di[s] = 1
            else:
                di[s] += 1
        if self.tar not in di:
            di[self.tar] = 0
        if di[self.tar] <= self.ma and di[self.tar] >= self.mi:
            return True
        return False

    def check_two(self):
        pos_1 = True; pos_2 = True
        if self.mi > 0 and \
            self.ma < len(self.string)+1:
            pos_1 = (self.string[self.mi-1] == self.tar)
            pos_2 = (self.string[self.ma-1] == self.tar)
        return pos_1 != pos_2

def load_data(filename):
    return [OneLine(line) for line in open(filename)]

def quiz_one(input):
    valid = 0
    for obj in input:
        if obj.check_one():
            valid += 1
    return valid

def quiz_two(input):
    valid = 0
    for obj in input:
        if obj.check_two():
            valid += 1
    return valid

if __name__ == '__main__':
    input = load_data('day_2.txt')
    res_1 = quiz_one(input)
    print (res_1)
    res_2 = quiz_two(input)
    print (res_2)
