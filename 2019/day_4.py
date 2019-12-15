#coding=utf8

def to_list(cand):
    clist = []
    while cand > 0:
        clist.insert(0, cand%10)
        cand = cand / 10
    return clist

def is_cand1(cand):
    clist = to_list(cand)
    has_double = False
    increase = True
    last_i = clist[0]
    for i in clist[1:]:
        if i == last_i:
            has_double = True
        if i < last_i:
            increase = False
            break
        last_i = i
    return has_double and increase

def is_cand2(cand):
    clist = to_list(cand)
    has_double = False
    len_2_double = False
    increase = True
    last_i = clist[0]
    max_double_len = 0
    for i in clist[1:]:
        if i == last_i:
            has_double = True
            max_double_len += 1
        else:
            if max_double_len == 1:
                len_2_double = True
            max_double_len = 0
            if i < last_i:
                increase = False
                break
        last_i = i
    if max_double_len == 1:
        len_2_double = True
    return has_double and increase and len_2_double

def part1(b_int, e_int):
    return len([i for i in range(b_int, e_int) if is_cand1(i)])

def part2(b_int, e_int):
    cands = [i for i in range(b_int, e_int) if is_cand2(i)]
    print (cands)
    return len(cands)

if __name__ == '__main__':
    print (part2(108457, 562041))