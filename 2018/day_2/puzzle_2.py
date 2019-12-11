#coding=utf8

def compare_two(str1, str2):
    length = len(str1)
    llist = [str1[i] for i in range(0, length) if str1[i] == str2[i]]
    return llist, len(llist)
    
if __name__ == '__main__':
    seq = [line.strip() for line in open("test.txt")]
    max_len = 0, max_sim = []
    seq_len = len(seq)
    for i in range(0, seq_len):
        for j in range(i+1, seq_len):
            sim, len_sim = compare_two(seq[i], seq[j])
            if len_sim > max_len:
                max_len = len_sim; max_sim = sim
    print "".join(max_sim)
