#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random
import math
import optimization

def hillclimb(domain, costf):
    # 無作為解の生成
    # 書籍では、
    # sol = [random.randint(domain[i][0], domain[i][0] )
    #        for i in range(len(domain))]
    # となってた。
    sol = [random.randint(domain[i][0], domain[i][1] )
           for i in range(len(domain))]
    # Main loop
    while 1:
        # 近傍解リストの生成
        neighbors = []
        for j in range(len(domain)):
            # 各方向に1ずつずらす
            if sol[j] > domain[j][0]:
                # sol[j+1:] → sol[j+1:]に訂正
                neighbors.append(sol[0:j] + [sol[j] - 1] + sol[j+1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] + 1] + sol[j+1:])
        # 近傍解中のベストを探す
        current = costf(sol)
        best = current
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                sol = neighbors[j]
        # 改善が見られなければそれが最高
        if best == current:
            break
        # print best
    return sol

if __name__ == '__main__':
    domain = [(0,9)]*(len(optimization.people)*2)
    s = hillclimb(domain, optimization.schedulecost)
    optimization.printschedule(s)
    cost = optimization.schedulecost(s)
    print('cost is %4s' % (cost))


