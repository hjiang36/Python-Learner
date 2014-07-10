__author__ = 'Killua'

# Bytelandian Coin
# For problem description, see
#   http://www.codechef.com/problems/COINS

import sys
from math import floor


def get_value(f2, f3, x):
    v = x >> f2
    for ii in range(0, f3):
        v = floor(v/3)
    return v


def get_coin(f2, f3, x):
    v = get_value(f2, f3, x)
    if v < 12:
        c_array[f2][f3] = v
    elif c_array[f2][f3] == 0:
        c_array[f2][f3] = get_coin(f2+1, f3, x) + get_coin(f2, f3+1, x) + get_coin(f2+2, f3, x)
    return c_array[f2][f3]

for l in sys.stdin:
    try:
        c_array = [[0 for x in range(30)] for x in range(30)]
        print(get_coin(0, 0, int(l)))
    except ValueError:
        break