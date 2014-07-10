__author__ = 'HJ'
 
# This is a potential solution to Prime Generator on code chef
# For the problem, see
#   http://www.codechef.com/problems/PRIME1
 
import sys
from math import ceil
 
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    if n < 9:
        return True
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
 
 
def gen_primes(n):
    # Generate all primes less or equal than n
    p = [2]
    for ii in range(3, n, 2):
        if is_prime(ii):
            p.append(ii)
    return p
 
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
 
    p = gen_primes(int(n**0.5)+1)
    seqLen = n - m + 1
    flag = [1] * seqLen
    for curP in p:
        sIndex = ceil(m/curP)*curP - m
        for ii in range(sIndex, seqLen, curP):
            flag[ii] = 0
        if sIndex + m == curP:
            flag[sIndex] = 1
 
    if m == 1:
        flag[0] = 0
    for ii in range(0, seqLen):
        if flag[ii] > 0:
            print(ii+m)
    t += 1
    print()
    if t > T:
        break 