#coding=utf8

init = "#..#.#..##......###...###"
#init = "##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#."
init = init.replace("#", "1").replace(".", "0")
init_ints = []; tmp = 0; zero = 0
while tmp < len(init):
    init_ints.append(int(init[tmp:min(tmp+32, len(init))], 2))
    tmp += 32

if __name__ == '__main__':
    rules = []
    for line in open("test.txt"):
        flist = line.strip().split(" => ")
        if flist[1] == "#":
            rules.append(int(flist[0].replace("#", "1").replace(".", "0"), 2))
    for generation in range(20):
        if (init_ints[0] >> 28) > 0:
            init_ints.insert(0, 0)
            zero += 1
        if init_ints[-1] & 7 > 0:
            init_ints.append(0)
        new_ints = []
        for i in range(len(init_ints)):
            sum = 0
            for j in range(27, -1, -1):
                if (init_ints[i] >> j) & 31 in rules:
                    sum += 2**(j + 2)
            if i > 0:
                if (init_ints[i] >> 28) + (init_ints[i-1] & 1) in rules:
                    sum += 2**(30)
                if (init_ints[i] >> 29) + (init_ints[i-1] & 2) in rules:
                    sum += 2**(31)
            if i < len(init_ints) - 1:
                if init_ints[i] & 15 + init_ints[i+1] >> 29 in rules:
                    sum += 2
                if init_ints[i] & 7 + init_ints[i+1] >> 28 in rules:
                    sum += 1
            print sum, "{0:032b}".format(sum).replace("1", "#").replace("0", ".")
            new_ints.append(sum)
        init_ints = new_ints
        print init_ints
            
