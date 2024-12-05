import collections
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    mid_line = lines.index("")
    conditions = lines[0:mid_line]
    printed = lines[mid_line + 1:]

    print(conditions, printed)

    G_pre = collections.defaultdict(set)
    for con in conditions:
        [a, b] = con.split("|")
        G_pre[a].add(b)


def check_row(nums):
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] not in G_pre[nums[j]]:
                return False
    return True


def fix_row(nums):
    while not check_row(nums):
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] not in G_pre[nums[j]]:
                    if nums[j] in G_pre[nums[i]]:
                        nums[i], nums[j] = nums[j], nums[i]
    return int(nums[len(nums) // 2])


def f():
    s = 0
    for row in printed:
        nums = row.split(",")
        if not check_row(nums):
            s += fix_row(nums)
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
