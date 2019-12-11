#coding=utf8

import numpy as np

players = 448
last = 7162800
#players = 17
#last = 1104

class Link:
    value = -1
    next = -1
    last = -1
    index = -1

class LinkList:
    link_list = []
    length = 0
    l_0 = Link(); l_0.value = 0; l_0.next = 1; l_0.last = 1; l_0.index = 0
    l_1 = Link(); l_1.value = 1; l_1.next = 0; l_1.last = 0; l_1.index = 1
    link_list.append(l_0); link_list.append(l_1)
    current = link_list[-1]

    def delete(self):
        for i in range(0, 7):
            self.current = self.link_list[self.current.last]
        self.link_list[self.current.last].next = self.current.next
        self.link_list[self.current.next].last = self.current.last
        value = self.current.value
        self.current = self.link_list[self.current.next]
        self.length -= 1
        return value

    def insert(self, value):
        self.current = self.link_list[self.current.next]
        l = Link()
        l.value = value
        l.index = len(self.link_list)
        l.next = self.current.next
        l.last = self.current.index
        self.link_list.append(l)
        self.current.next = l.index
        self.link_list[l.next].last = l.index
        self.current = self.link_list[-1]
        self.length += 1

    def debug(self):
        start = self.link_list[0]
        llist = []
        while start.next != 0:
            llist.append(start.value)
            start = self.link_list[start.next]
        print llist

if __name__ == '__main__':
    scores = np.zeros(players)
    ll = LinkList(); player = 0; marble = 2
    while marble < last + 1:
        player = (player + 1) % players
        if marble % 23 == 0:
            scores[player] += marble
            scores[player] += ll.delete()
            marble += 1
            continue
        ll.insert(marble)
        marble += 1
    print np.argmax(scores), max(scores)
