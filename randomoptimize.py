#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random
import math
import optimization

def randomoptimize(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        # 無作為解の生成
        r = [random.randint(domain[i][0], domain[i][1])
             for i in range(len(domain))]

        # コストの取得
        cost = costf(r)

        # 最良解と比較
        if cost < best:
            best = cost
            bestr = r
    return bestr # 書籍にはrと書かれていた

if __name__ == '__main__':
    domain = [(0,9)]*(len(optimization.people)*2) # 書籍には(0.8)と書かれていた
    s = randomoptimize(domain, optimization.schedulecost)
    optimization.printschedule(s)
    cost = optimization.schedulecost(s)
    print('cost is %4s' % (cost))

