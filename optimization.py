#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random
import math

people = [('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt', 'MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')]

# ニューヨークのラガーディア空港
destination = 'LGA'

flights = {}
for line in file('schedule.txt'):
    origin, dest, depart, arrive, price =  line.strip().split(',')
    flights.setdefault((origin,dest),[])
    
    # リストのフライトの詳細を追加
    flights[(origin, dest)].append((depart, arrive, int(price)))

# 時刻を一日の中で何分目かを計算
def getminutes(t):
    x = time.strptime(t, '%H:%M')
    return x[3]*60 + x[4]

# 解の出力
def printschedule(r):
    for d in range(len(r)/2):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin, destination)][int(r[d*2])]
        ret = flights[(destination, origin)][int(r[d*2+1])]
        print('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin,
                                                      out[0], out[1], out[2],
                                                      ret[0], ret[1], ret[2]))


def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    earliestdep = 24 * 60

    for d in range(len(sol)/2):
        # 行き(outbound)と帰り(return)のフライトを得る
        origin = people[d][1]
        outbound = flights[(origin, destination)][int(sol[d*2])]
        returnf = flights[(destination, origin)][int(sol[d*2+1])]

        # 運賃の総額total priceは出立便と帰宅便すべての運賃
        totalprice += outbound[2]
        totalprice += returnf[2]

        # 最も遅い到着と最も早い出発を記録
        if latestarrival < getminutes(outbound[1]):
            latestarrival = getminutes(outbound[1])
        if earliestdep > getminutes(returnf[0]):
            earliestdep = getminutes(returnf[0])

        # 最後の人が到着するまで全員空港で待機
        # 帰りも空港にみんなで来て自分の便を待たねばならない
        totalwait = 0
        for d in range(len(sol)/2):
            origin = people[d][1]
            outbound = flights[(origin, destination)][int(sol[d*2])]
            returnf = flights[(destination, origin)][int(sol[d*2+1])]
            totalwait += latestarrival - getminutes(outbound[1])
            totalwait += getminutes(returnf[0]) - earliestdep

        # この解ではレンタカーの追加料金が必要か
        if latestarrival < earliestdep:
            totalprice += 50
    return totalprice + totalwait

if __name__ == '__main__':
    s = [4,4,4,2,2,6,6,5,5,6,6,0]
    printschedule(s)
    cost = schedulecost(s)
    print('cost is %4s' % (cost))

