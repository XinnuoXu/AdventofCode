#coding=utf8

import re
pattern = re.compile(r'\#(?P<ID>\d+) @ (?P<fleft>\d+),(?P<ftop>\d+): (?P<wide>\d+)x(?P<tall>\d+)')

if __name__ == '__main__':
    # Initialization
    fabric = [[0 for i in range(1000)] for j in range(1000)]
    id_tags = [i for i in range(1336)]
    # Processing
    for line in open("test.txt"):
        m = pattern.match(line.strip())
        id = int(m.group("ID"))
        fleft = int(m.group("fleft"))
        ftop = int(m.group("ftop"))
        wide = int(m.group("wide"))
        tall = int(m.group("tall"))
        for i in range(fleft, fleft + wide):
            for j in range(ftop, ftop + tall):
                if fabric[i][j] == 0:
                    fabric[i][j] = id
                else:
                    id_tags[fabric[i][j]] = 0
                    id_tags[id] = 0
    print sum(id_tags)
