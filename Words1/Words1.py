__author__ = 'Killua'


# Problem description, see:
#   http://www.codechef.com/problems/WORDS1

T = input()
T = int(T)

for _ in range(T):
    n = input()
    n = int(n)
    c = [0]*27  # counter for start and end
    encountered = [False]*27
    s_word = [False]*27  # special words
    flag = True
    for _ in range(n):
        word = input()
        s_index = ord(word[0]) - 97  # ord('a') = 97
        e_index = ord(word[len(word)-1]) - 97
        if not encountered[s_index]:
            encountered[s_index] = True
            if s_index == e_index:
                s_word[s_index] = True
                continue
            flag = False
        if not encountered[e_index]:
            encountered[e_index] = True
        c[s_index] += 1
        c[e_index] -= 1

    # check for special words
    result = True
    if not flag:
        # check all special words occurred in other words
        for i in range(27):
            if s_word[i] and not encountered[i]:
                result = False
                break

        if not result:
            print("The door cannot be opened.")
            continue

        # check common words
        x = 0
        for v in c:
            x += abs(v)
        result = (x <= 2)
    elif sum(s_word) > 1:
        result = False

    if result:
        print("Ordering is possible.")
    else:
        print("The door cannot be opened.")