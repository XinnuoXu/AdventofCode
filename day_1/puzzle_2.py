#coding=utf8

if __name__ == '__main__':
    seq = [int(line.strip()) for line in open("test.txt")]
    total = 0
    sum_list = set([0])
    done = False
    while not done:
        for item in seq:
            total += item
            if total in sum_list:
                print total
                done = True
                break
            sum_list.add(total)
