import timeit
from collections import defaultdict, deque
from functools import cache

with open('2025/11/test.txt') as f:
    lines = f.read().splitlines()
    edges = defaultdict(set)
    for line in lines:
        input = line.split()[0][:-1]
        for out in line.split()[1:]:
            edges[input].add(out)
    
    # print(edges)

# @cache
# def dfs(curr_node, target_node):
#     if curr_node == target_node:
#         return 1
#     else:
#         return sum([dfs(neigh, target_node) for neigh in edges[curr_node]])

# def f():
#     ans = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out") \
#         + dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")

#     print(ans)
#     print(f"Cache info: {dfs.cache_info()}")

def f2():
    memo = {}  # Shared memoization keyed on (node, target_node)

    def dfs_iterative(start_node, target_node):
        # Check if we've already computed this
        if (start_node, target_node) in memo:
            return memo[(start_node, target_node)]

        local_memo = {}  # Local results for this target
        stack = [start_node]
        in_progress = set()

        while stack:
            node = stack[-1]

            # Check global memo first
            if (node, target_node) in memo:
                local_memo[node] = memo[(node, target_node)]
                stack.pop()
                continue

            # If already computed locally, pop and continue
            if node in local_memo:
                stack.pop()
                continue

            # Base case: reached target
            if node == target_node:
                local_memo[node] = 1
                stack.pop()
                continue

            # Check if we're revisiting this node after processing children
            if node in in_progress:
                # All children have been processed, compute result
                result = 0
                for neigh in edges[node]:
                    if neigh in local_memo:
                        result += local_memo[neigh]
                    elif (neigh, target_node) in memo:
                        result += memo[(neigh, target_node)]
                local_memo[node] = result
                stack.pop()
                in_progress.remove(node)
            else:
                # First visit: mark in progress and add children to stack
                in_progress.add(node)
                for neigh in edges[node]:
                    if neigh not in local_memo and (neigh, target_node) not in memo:
                        stack.append(neigh)

        # Store all local results in global memo
        for node, value in local_memo.items():
            memo[(node, target_node)] = value

        return local_memo.get(start_node, 0)

    ans = dfs_iterative("svr", "dac") * dfs_iterative("dac", "fft") * dfs_iterative("fft", "out") \
        + dfs_iterative("svr", "fft") * dfs_iterative("fft", "dac") * dfs_iterative("dac", "out")

    print(ans)
    print(f"Memo size: {len(memo)} entries")


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f2(), number=iters)
    print(f"{x / iters: 0.20f} s")
