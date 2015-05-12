__author__ = 'Killua'

import sys


def main():
    # number of test cases
    t = int(sys.stdin.readline())

    # allocate some space for results
    result = [0 for ii in range(101)]
    result[1] = 1
    s = 1
    for ii in range(0, t):
        n = int(sys.stdin.readline())
        if n > s:
            for jj in range(s+1, n+1):
                result[jj] = result[jj-1]*jj
            s = n
        print(result[n])

if __name__ == '__main__':
    main()