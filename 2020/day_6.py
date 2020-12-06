#coding=utf8

def load_data(filename):
    groups = []; group = []
    for line in open(filename):
        line = line.strip()
        line = list(line)
        if len(line) == 0:
            groups.append(group)
            group = []
        else:
            group.append(line)
    if len(group) != 0:
        groups.append(group)
    return groups

def quiz_one(groups):
    question_count = 0
    for group in groups:
        question_count += len(set().union(*group))
    return question_count

def quiz_two(groups):
    question_count = 0
    for group in groups:
        question_count += len(set(group[0]).intersection(*group))
    return question_count

if __name__ == '__main__':
    input = load_data('day_6.txt')
    res_1 = quiz_one(input)
    print (res_1)
    res_2 = quiz_two(input)
    print (res_2)
