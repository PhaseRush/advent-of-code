import functools
import time
from collections import Counter

ord = ['A', 'K', 'Q', 'T', '09', '08', '07', '06', '05', '04', '03', '02', 'J']


def get_highest_face(faces):
    if len(faces) == 1:
        return faces[0]

    if ord.index(faces[0]) > ord.index(faces[1]):
        return faces[0]
    else:
        return faces[1]


def get_type(a: str):
    a_freq = Counter(a)
    sort = sorted(a_freq.values(), reverse=True)
    has_joker = 'J' in a_freq.keys()

    if not has_joker:
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
    else:
        most_freq_faces = []
        for k, v in a_freq.items():
            if v == sort[0] and k != 'J':  # may fail if 03 Js
                most_freq_faces.append(k)
        if not most_freq_faces:
            most_freq_faces = list(a.replace('J', ''))
            if not most_freq_faces:  # all Js
                return 7

        face_to_replace = get_highest_face(most_freq_faces)

        return get_type(a.replace('J', face_to_replace))

    print("invalid score", a, type(a))


def compare(a, b):
    a = a[0]
    b = b[0]

    a_type = get_type(a)
    b_type = get_type(b)

    if a_type == b_type:  # find first highest
        for i in range(5):
            a_ord = ord.index(a[i])
            b_ord = ord.index(b[i])
            if a_ord != b_ord:
                return b_ord - a_ord
    else:
        return a_type - b_type

    print("invalid compare")


with open('input.txt') as f:
    lines = f.read().splitlines()

    start = time.process_time_ns()

    hands = [(x.split()[0], int(x.split()[1])) for x in lines]

    # print(hands)

    ordered = sorted(hands, key=functools.cmp_to_key(compare))
    # print(ordered)

    score = 0
    for x in range(len(ordered)):
        score += (x + 1) * ordered[x][1]
    print(score)

    print((time.process_time_ns() - start) / 10e6, " ms")
