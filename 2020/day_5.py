#coding=utf8

def load_data(filename):
    mapping = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}
    seat_nums = []
    for line in open(filename):
        line = line.strip()
        line = ''.join([mapping[l] for l in line])
        seat_num = int(line, base=2)
        seat_nums.append(seat_num)
    return seat_nums

if __name__ == '__main__':
    seat_nums = load_data('day_5.txt')

    res_1 = max(seat_nums)
    print (res_1)

    '''
    # O(nlogn)
    res_2 = seat_nums[0]
    seat_nums.sort()
    for i, num in enumerate(seat_nums):
        if num+1 != seat_nums[i+1]:
            res_2 = num+1
            break
    print (res_2)
    '''

    # O(n)
    mi = min(seat_nums)
    ma = max(seat_nums)
    res_2 = mi
    seat_nums = set(seat_nums)
    for i in range(mi, ma):
        if i not in seat_nums:
            res_2 = i
            break
    print (res_2)

    # Or with extra space O(n)
    new_set = set(range(mi, ma))
    res_2 = new_set.difference(seat_nums)
    print (res_2)
