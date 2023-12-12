import functools
import timeit
from multiprocessing import Pool

with open('input.txt') as f:
    lines = f.read().splitlines()
    lines = [x.split() for x in lines]
    lines = [(x[0], list(map(int, x[1].split(',')))) for x in lines]

can_begin_run = {'?', '#'}
cant_begin_run = {'?', '.'}


@functools.cache
def solve(s, curr_run_idx, remain):
    if curr_run_idx and len(remain) == 0:  # can't make enough choices
        return 0
    if not s:
        if curr_run_idx is None and len(remain) == 0:
            return 1  # outside last run, no more to search
        if len(remain) == 1 and curr_run_idx == remain[0]:
            return 1  # currently on the last char of the last run
        return 0

    choices = 0
    if curr_run_idx:  # currently in a run
        if s[0] == '.':
            if curr_run_idx != remain[0]:  # curr run ended and not the same length as needed
                return 0
            choices += solve(s[1:], None, remain[1:])  # reset run, go next

        if s[0] == '?' and curr_run_idx == remain[0]:  # forced to end curr run
            choices += solve(s[1:], None, remain[1:])
        if s[0] == '#' or s[0] == '?':  # choose to continue run
            choices += solve(s[1:], curr_run_idx + 1, remain)

    else:  # currently not in a run
        if s[0] in can_begin_run:  # solve if begin run
            choices += solve(s[1:], 1, remain)
        if s[0] in cant_begin_run:  # solve if dont begin run
            choices += solve(s[1:], None, remain)

    return choices


def start(input):
    return solve(input[0], input[1], input[2])


inputs = []

for line in lines:
    unfolded = line[0] + ''.join(['?' + line[0] for _ in range(4)])
    inputs.append((unfolded, None, tuple(line[1]) * 5))


def f():
    with Pool() as pool:
        return sum(pool.map(start, inputs))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
