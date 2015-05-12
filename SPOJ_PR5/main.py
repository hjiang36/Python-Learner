__author__ = 'Killua'

import sys


def next_palindrome(s):
    """
    finding next palindrome for string s
    :param s: long integer represented as string
    :return: next palindrome represented as string
    """
    # length of string
    l = len(s)
    s = list(s)
    p_left = 0
    p_right = l - 1
    status = False

    if l == 1:
        return '11'

    while p_left < p_right:
        if s[p_left] > s[p_right]:
            status = True
        elif s[p_left] < s[p_right]:
            status = False
        s[p_right] = s[p_left]
        p_left += 1
        p_right -= 1

    if status:
        return ''.join(s)

    while p_right >= 0:
        if s[p_right] < '9':
            s[p_right] = str(int(s[p_right]) + 1)
            s[p_left] = s[p_right]
            break
        else:
            s[p_left] = s[p_right] = '0'
            p_left += 1
            p_right -= 1

    if p_right < 0:
        s.insert(0, '1')
        s[-1] = '1'
    return ''.join(s)

def main():
    # number of test cases
    t = int(sys.stdin.readline())

    # process for each test cases
    for _ in range(t):
        s = sys.stdin.readline()
        if s[-1] == '\n':
            s = s[:-1]
        print(next_palindrome(s))


if __name__ == '__main__':
    main()