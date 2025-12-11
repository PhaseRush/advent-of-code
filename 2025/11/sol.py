import timeit
from collections import defaultdict, deque


with open('2025/11/test.txt') as f:
    lines = f.read().splitlines()
    edges = defaultdict(set)
    for line in lines:
        input = line.split()[0][:-1]
        for out in line.split()[1:]:
            edges[input].add(out)
    
    print(edges)

    # lines = [list(row) for row in lines]



# def f():
#     num_paths = 0
#     paths = set()
    
#     q = deque([("you")])

#     while q:
#         curr_path = q.popleft()
#         curr_node = curr_path[-1]
#         curr_neighbours = edges[curr_node]
#         print(f"{curr_path} {curr_node}, {curr_neighbours}")
#         for neigh in curr_neighbours:
#             if (neigh == "out"):
#                 paths.add(curr_path + neigh)
#             else:
#                 q.append(tuple(curr_path + neigh))

#     print(len(paths))

def dfs(curr_node):
    if curr_node == "out":
        return 1
    else:
        return sum([dfs(neigh) for neigh in edges[curr_node]])

def f():
    ans = dfs("you")
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.20f} s")
