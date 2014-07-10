__author__ = 'Killua'

# Problem description, see:
#    http://www.codechef.com/problems/MIXTURES

import sys

for line in sys.stdin:
    n = int(line)

    line = input()
    v = line.split()
    smoke = [[0 for x in range(n)] for x in range(n)]
    residual = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        v[i] = int(v[i])

    # Compute residual
    # residual is not depend on the sequence of mixture
    for i in range(0, n):
        for j in range(i, n):
            residual[i][j] = sum(v[i:(j+1)]) % 100

    # dynamic programming
    # smoke[i][j] = min(v[i] * residual[i+1][j] + smoke[i+1][j], v[j] * residual[i][j-1] + smoke[i][j-1])
    for d in range(1, n):
        for i in range(0, n-d):
            j = i + d
            min_value = float("inf")
            for k in range(i, j):
                min_value = min(min_value, smoke[i][k] + smoke[k+1][j] + residual[i][k] * residual[k+1][j])
            smoke[i][j] = min_value

    # print
    print(smoke[0][n-1])