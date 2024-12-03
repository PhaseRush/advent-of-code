import timeit
import re
import math

with open('input.txt') as f:
    lines = f.read().splitlines()


def f():
    s = 0
    l = ''.join(lines)
    for g in re.finditer('mul\(\d+,\d+\)', l):
        curr_str = l[g.start(0):g.end(0)]
        last_do = list(re.finditer('do\(\)', l[0:g.start(0)]))
        last_dont = list(re.finditer('don\'t\(\)', l[0:g.start(0)]))
        last_do_idx = last_do[-1].start(0) if last_do else 0
        last_dont_idx = last_dont[-1].start(0) if last_dont else -1
        curr_s = math.prod(map(int, re.findall('\d+', curr_str)))
        if last_do_idx > last_dont_idx:
            s += curr_s
    print(s)
    return s


print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
