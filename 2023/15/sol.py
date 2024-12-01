import functools
import timeit
from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()
    strs = lines[0].split(',')


@functools.cache
def h(s: str):
    # return functools.reduce(lambda val, c: ((val + ord(c)) * 17) % 256, s, 0)
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


def f():
    # print(sum([h(s) for s in strs]))
    lenses = [defaultdict(int) for _ in range(256)]

    for s in strs:
        if '-' in s:
            label, focus = s.split('-')
            box_id = h(label)
            box = lenses[box_id]
            if label in box:
                del box[label]
        else:
            label, focus = s.split('=')
            box_id = h(label)
            box = lenses[box_id]
            box[label] = focus

    total = 0
    for b_id, box in enumerate(lenses, -1):
        for l_id, (_, focus) in enumerate(box.items(), -1):
            total += (2 + b_id) * (2 + l_id) * int(focus)
    # print(total)
    return total


if __name__ == '__main__':
    iters = 1000
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} ms")
