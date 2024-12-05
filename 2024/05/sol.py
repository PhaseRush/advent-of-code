import collections
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    mid_line = lines.index("")
    conditions = lines[0:mid_line]
    printed = lines[mid_line + 1:]

    print(conditions, printed)

    G_pre = collections.defaultdict(set)
    G_post = collections.defaultdict(set)
    for con in conditions:
        [a, b] = con.split("|")
        G_pre[a].add(b)
        G_post[b].add(a)


def check_row(nums):
    for i in range(len(nums)):
        # check i can be after every prev number
        for j in range(0, i):
            if nums[i] not in G_pre[nums[j]]:
                print("no rule: ", nums[j] + "|" + nums[i])
                return 0
            print("found rule:", nums[j] + "|" + nums[i])
    print("ret ", nums[len(nums) // 2], len(nums)//2)
    return int(nums[len(nums) // 2])


def f():
    s = 0
    for row in printed:
        nums = row.split(",")
        s += check_row(nums)
    print(s)
    return s

# print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
