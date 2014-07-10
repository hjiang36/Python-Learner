__author__ = 'HJ'

# This is a potential solution to Prime Generator on code chef
# For the problem, see
#   http://www.codechef.com/problems/PRIME1

import sys


def factorize(n):
    p_list = []
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            p_list.append(x)
    return p_list

t = 0
T = 0

for line in sys.stdin:
    if t == 0:
        T = int(line)
        t += 1
        continue
    m, n = line.split()
    m = int(m)
    n = int(n)

    if m < 3:
        print(2)
        m = 3
    if not m & 1:
        m += 1
    seqLen = n - m + 1
    flag = [1] * seqLen
    for index in range(0, seqLen, 2):
        if not flag[index]:
            continue
        num = m + index
        p_list = factorize(num)
        if not p_list:
            print(num)
            p_list = [num]
        for p in p_list:
            for ii in range(index, seqLen, p):
                flag[ii] = 0
    t += 1
    print()
    if t > T:
        break