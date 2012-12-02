#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random
import math
import optimization

if __name__ == '__main__':
    s = [4,4,4,2,2,6,6,5,5,6,6,0]
    # s = [7,5,2,3,1,6,1,6,7,1,0,3]
    # s = [7,2,2,2,3,3,2,3,5,2,0,8]
    # s = [0,4,0,3,8,8,4,4,8,5,6,1]
    # s = [5,8,0,2,8,8,8,2,1,6,6,8]
    
    optimization.printschedule(s)
    cost = optimization.schedulecost(s)
    print('cost is %4s' % (cost))


