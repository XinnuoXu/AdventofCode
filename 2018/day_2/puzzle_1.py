#coding=utf8

def read_line(line):
    l_dict = {}
    for letter in line:
        if letter not in l_dict:
            l_dict[letter] = 1
        else:
            l_dict[letter] += 1
    two_count = 0
    three_count = 0
    for item in l_dict:
        if l_dict[item] == 2:
            two_count += 1
        elif l_dict[item] == 3:
            three_count += 1
    return int(two_count >= 1), int(three_count >= 1)
    
if __name__ == '__main__':
    seq = [line.strip() for line in open("test.txt")]
    num_2 = 0; num_3 = 0
    for line in seq:
        list_2, list_3 = read_line(line)
        num_2 += list_2
        num_3 += list_3
    print num_3 * num_2
