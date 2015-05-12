__author__ = 'Killua'

import sys
import math


def is_prime(n, p_list):
    if n & 0x1 == 0:
        return False
    thresh = round(math.sqrt(n))
    for ii in p_list:
        if ii > thresh:
            break
        if n % ii == 0:
            return False
    return True


def main():
    # Read number of test cases
    t = int(sys.stdin.readline())

    # Generate prime list
    # This is pre-computation and should be done only once for all test cases
    p_list = []
    for k in range(3, 32000, 2):
        if is_prime(k, p_list):
            p_list.append(k)

    # Generate prime number list for each test case
    for _ in range(t):
        # Read in the number range
        m, _, n = sys.stdin.readline().partition(' ')
        m = int(m)
        n = int(n)

        # Init result list
        if m <= 2 <= n:
            print(2)

        # Convert m and n to odd number
        if n & 0x1 == 0:
            n -= 1
        if m & 0x1 == 0:
            m += 1

        # Compute residual list
        thresh = round(math.sqrt(n)) + 1

        if n < 32000:
            for ii in p_list:
                if m <= ii <= n:
                    print(ii)
        elif m > 32000:
            residual = [m % x for x in p_list if x <= thresh]
            for ii in range(m, n+1, 2):
                if all([i > 0 for i in residual]):
                    print(ii)
                for jj, v in enumerate(residual):
                    residual[jj] = (v + 2) % p_list[jj]
        else:
            for ii in p_list:
                if m <= ii:
                    print(ii)
            m = 32001
            residual = [m % x for x in p_list if x <= thresh]
            for ii in range(m, n+1, 2):
                if all([i > 0 for i in residual]):
                    print(ii)
                for jj, v in enumerate(residual):
                    residual[jj] = (v + 2) % p_list[jj]

        # print empty line between cases
        print()


if __name__ == '__main__':
    main()