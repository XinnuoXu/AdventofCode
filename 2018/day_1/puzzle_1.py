#coding=utf8

if __name__ == '__main__':
    seq = [int(line.strip()) for line in open("test.txt")]
    print sum(seq)
