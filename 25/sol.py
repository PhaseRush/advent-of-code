import math
import timeit
from collections import defaultdict
import networkx as nx

with open('input.txt') as f:
    lines = [line.split(": ") for line in f.read().splitlines()]

    G = nx.Graph()
    # graph = defaultdict(set)
    for node, neighbours in lines:
        neighbours = neighbours.split(" ")
        for ns in neighbours:
            # graph[node].add(ns)
            # graph[ns].add(node)
            G.add_edge(node, ns)


def f():
    min_cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(min_cuts)
    components = nx.connected_components(G)
    print(math.prod([len(x) for x in components]))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
