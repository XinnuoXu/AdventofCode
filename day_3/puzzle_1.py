#coding=utf8

import re
pattern = re.compile(r'\#(?P<ID>\d+) @ (?P<fleft>\d+),(?P<ftop>\d+): (?P<wide>\d+)x(?P<tall>\d+)')

if __name__ == '__main__':
    # Initialization
    fabric = [[0 for i in range(1000)] for j in range(1000)]
    # Processing
    for line in open("test.txt"):
        m = pattern.match(line.strip())
        id = m.group("ID")
        fleft = int(m.group("fleft"))
        ftop = int(m.group("ftop"))
        wide = int(m.group("wide"))
        tall = int(m.group("tall"))
        for i in range(fleft, fleft + wide):
            for j in range(ftop, ftop + tall):
                fabric[i][j] += 1
    print sum([1 for i in range(1000) for j in range(1000) if fabric[i][j] > 1])
                
