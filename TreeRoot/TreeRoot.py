__author__ = 'Killua'


# Problem description, see:
#   http://www.codechef.com/problems/TREEROOT

T = input()

for t in range(int(T)):
    N = input()
    N = int(N)
    s = 0  # sum of id - child_sum
    for n in range(N):
        node_id, child_sum = input().split()
        s = s + int(node_id) - int(child_sum)
    print(s)