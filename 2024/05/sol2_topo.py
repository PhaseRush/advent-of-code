import collections
import timeit

import networkx
from networkx import DiGraph

with open('input.txt') as f:
    lines = f.read().splitlines()
    mid_line = lines.index("")
    conditions = lines[0:mid_line]
    printed = lines[mid_line + 1:]

    print(conditions, printed)

    G_pre = collections.defaultdict(set)
    edges = set()
    for con in conditions:
        [a, b] = con.split("|")
        G_pre[a].add(b)
        edges.add((a, b))


def f():
    s = 0

    for row in printed:
        nums = row.split(",")
        graph = DiGraph((a, b) for a, b in edges if a in nums and b in nums)
        sorted = list(networkx.topological_sort(graph))
        if sorted != nums:
            s += int(sorted[len(sorted) // 2])

    # print(s)
    return s


if __name__ == '__main__':
    iters = 1000
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
