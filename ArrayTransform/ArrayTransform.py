__author__ = 'Killua'


# Problem description, see:
#  http://www.codechef.com/problems/ARRAYTRM

t = int(input())
for case in range(t):
    n,k = input().split()
    n,k = int(n),int(k)
    a = input().split()
    c = [0]*(k+1)

    for i in range(n):
        c[int(a[i]) % (k+1)] += 1

    result = "NO"
    for a in c:
        if a >= n-1:
            result = "YES"
    print(result)