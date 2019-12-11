#coding=utf8

#init = "#..#.#..##......###...###"
init = "##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#."

if __name__ == '__main__':
    rules = [line.strip().split(" => ")[0] for line in open("test.txt") if line.strip().split(" => ")[1] == "#"]
    zero = 0
    for generation in range(20):
        new_gen = []
        init = "...." + init + "...."
        for i in range(2, len(init)-2):
            str = init[i-2:i+3]
            if str in rules:
                new_gen.append("#")
            else:
                new_gen.append(".")
        init = "".join(new_gen)
        zero += 2
    sum = 0
    for i in range(len(init)):
        if init[i] == "#":
            sum += (i - zero)
    print sum
                
