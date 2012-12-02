#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random
import math
import optimization

def annealingoptimize(domain, costf, T=10000.0, cool=0.95, step=1):
    # ランダムな値で解を初期化
    vec = [float(random.randint(domain[i][0],domain[i][1]))
           for i in range(len(domain))]

    while T > 0.1:
        # インデックスを一つ選ぶ
        i = random.randint(0, len(domain)-1)

        # インデックスの値に加える変更の方向を選ぶ
        direct = random.randint(-step, step)

        # 値を変更したリスト(解)を生成
        vecb = vec[:]
        vecb[i] += direct
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]

        # 現在解と生成解のコストを算出
        ea = costf(vec)
        eb = costf(vecb)
        p = pow(math.e, -abs(eb-ea)/T)

        # 生成解がベターまたは確率的に採用？
        if ( eb < ea or random.random() < p):
            vec = vecb

        # 温度のを下げる
        T = T*cool

    return vec

if __name__ == '__main__':
    domain = [(0,9)]*(len(optimization.people)*2) # 書籍には(0.8)と書かれていた
    s = annealingoptimize(domain, optimization.schedulecost)
    optimization.printschedule(s)
    cost = optimization.schedulecost(s)
    print('cost is %4s' % (cost))


