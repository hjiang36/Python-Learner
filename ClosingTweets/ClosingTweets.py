__author__ = 'Killua'


# Problem description, see:
#   http://www.codechef.com/problems/TWTCLOSE

line = input()
n, k = line.split()
n, k = int(n), int(k)

is_open = [0]*n
for ii in range(k):
    line = input()
    line = line.split()
    if len(line) == 1:  # Close all
        is_open = [0]*n
    else:  # Click X
        x = int(line[1])
        is_open[x-1] = 1 - is_open[x-1]
    print(sum(is_open))