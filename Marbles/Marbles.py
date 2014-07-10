__author__ = 'Killua'

# Problem description:
#   http://www.codechef.com/problems/MARBLES

import sys

t = 0
T = 0

for line in sys.stdin:
    if t == 0:
        T = int(line)
        t += 1
        continue
    n, k = line.split()
    n = int(n)
    k = int(k)

    # Totally we need select n-k from k kinds of marbles
    # That is x1 + x2 + ... + xk = n - k
    # Equivalently, we select k-1 from n-1: (n-1)! / (n-k)!(k-1)!
    endPts = min(n-k, k-1)
    result = 1
    for ii in range(1,endPts+1):
        result = result * (n-ii) / ii

    print(round(result))

    t += 1
    if t > T:
        break