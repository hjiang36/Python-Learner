__author__ = 'Killua'

# For problem description, see:
#   http://www.codechef.com/problems/PALIN

import sys

t = 0
T = 0

for line in sys.stdin:
    if t == 0:
        T = int(line)
        t += 1
        continue

    # First compute the center position
    n = len(line) - 2
    c = int(n/2)
    m = c
    line = list(line)
    line = line[:n+1]

    # Check whether or not we need to adjust
    ii = 0
    flag = True
    for ii in range(c+1, n+1):
        if line[ii] < line[n-ii]:  # don't need to adjust
            flag = False
            break
        elif line[ii] > line[n-ii]:  # adjust
            m = c
            while line[m] == '9':
                line[m] = '0'
                m -= 1
            line[m] = str(int(line[m])+1)
            flag = False
            break

    if flag:
        m = c
        while line[m] == '9':
            line[m] = '0'
            m -= 1
            if m < 0:
                print('1', end='')
                print('0'*n, end='')
                print('1')
                break
        line[m] = str(int(line[m])+1)

    if m < 0:
        t += 1
        if t > T:
            break
        continue

    # print
    l = "".join(line[:c+1])
    if n == 0:
        print(l)
    elif n & 1:
        print(l, end='')
        print(l[::-1])
    else:
        print(l, end='')
        l = l[:c]
        print(l[::-1])

    t += 1
    if t > T:
        break
