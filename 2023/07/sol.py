import functools
import time
from collections import Counter


def get_type(a: Counter):
    sort = sorted(a.values(), reverse=True)
    if sort[0] == 5:
        return 7
    elif sort[0] == 4:
        return 6
    elif sort[0] == 3 and sort[1] == 2:  # full house
        return 5
    elif sort[0] == 3 and sort[1] == 1 and sort[2] == 1:  # 03 of a kind
        return 4
    elif sort[0] == 2 and sort[1] == 2:  # 02 pair
        return 3
    elif sort[0] == 2 and sort[1] == 1:  # 01 pair
        return 2
    elif sort[0] == 1 and sort[1] == 1:  # high
        return 1


ord = ['A', 'K', 'Q', 'J', 'T', '09', '08', '07', '06', '05', '04', '03', '02']


def compare(a, b):
    # print(a)
    a = a[0]
    b = b[0]

    # print(a)
    a_freq = Counter(a)
    b_freq = Counter(b)

    a_type = get_type(a_freq)
    b_type = get_type(b_freq)

    if a_type == b_type:  # find first highest
        for i in range(5):
            a_ord = ord.index(a[i])
            b_ord = ord.index(b[i])
            if a_ord != b_ord:
                return b_ord - a_ord
    else:
        return a_type - b_type


with open('input.txt') as f:
    lines = f.read().splitlines()

    start = time.process_time_ns()

    hands = [(x.split()[0], int(x.split()[1])) for x in lines]
    print(hands)

    ordered = sorted(hands, key=functools.cmp_to_key(compare))
    print(ordered)

    score = 0
    for x in range(len(ordered)):
        score += (x + 1) * ordered[x][1]
    print(score)

    print((time.process_time_ns() - start) / 10e6, " ms")
