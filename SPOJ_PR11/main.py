import sys
import math

__author__ = 'Killua'


def main():
    n = int(sys.stdin.readline())
    for ii in range(0, n):
        k = int(sys.stdin.readline())
        r = 0
        while k > 0:
            k = math.floor(k/5)
            r += k
        print(int(r))


if __name__ == "__main__":
    main()