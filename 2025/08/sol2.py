import math
from collections import defaultdict
import timeit

# Read input
with open('2025/08/test.txt') as f:
    lines = f.read().splitlines()
    # Parse junction boxes
    boxes = []
    for line in lines:
        if line:
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return  # Already in same circuit
        self.parent[px] = py

    def get_component_sizes(self):
        """Returns a list of all component sizes"""
        sizes = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            sizes[root] += 1
        return list(sizes.values())

    def num_components(self):
        """Returns the number of distinct components"""
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)


def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2


def f():
    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = distance(boxes[i], boxes[j])
            pairs.append((dist, i, j))

    print(f"Total pairs: {len(pairs)}")

    pairs.sort()

    uf = UnionFind(len(boxes))

    for i in range(len(pairs)):
        dist, box1, box2 = pairs[i]

        # Check if they're already connected
        if uf.find(box1) != uf.find(box2):
            uf.union(box1, box2)

            # Check if we now have only 1 component
            if uf.num_components() == 1:
                # This was the connection that unified everything
                x1 = boxes[box1][0]
                x2 = boxes[box2][0]
                ans = x1 * x2
                print(ans)
                break

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")