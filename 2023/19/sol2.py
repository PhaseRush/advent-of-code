import math
import timeit
from collections import defaultdict


def op_filter(val, op):
    if op == '>':
        return lambda var: var > val
    else:
        return lambda var: var < val


with open('input.txt') as f:
    lines = f.read().splitlines()
    empty = lines.index("")
    wfs_lines = lines[0:empty]
    wfs = defaultdict(list)
    for wf in wfs_lines:
        name, details = wf.split("{")
        details_list = details[:-1].split(",")
        checks = []
        for check in details_list:
            spl = check.split(':')
            if len(spl) == 1:
                checks.append(spl[0])
                continue
            var = spl[0][0]
            op = spl[0][1]
            val = int(spl[0][2:])
            checks.append((spl[1], var, op_filter(val, op)))
        wfs[name] = checks


def recurse(wf, ranges):
    if wf == 'R':
        return 0
    elif wf == 'A':
        return math.prod([len(v) for k, v in ranges.items()])

    checks = wfs[wf]
    count = 0
    for check in checks:
        if isinstance(check, tuple):
            next_wf = check[0]
            curr_param = check[1]
            filter_check = check[2]

            for param, range in ranges.items():
                if param == curr_param:
                    filtered = list(filter(filter_check, range))
                    if len(filtered):
                        new_ranges = ranges.copy()
                        new_ranges[param] = filtered
                        count += recurse(next_wf, new_ranges)
                    ranges[param] = list(x for x in range if not filter_check(x))
        else:
            count += recurse(check, ranges)

    return count


def f():
    answer = recurse('in', {
        'x': range(1, 4001),
        'm': range(1, 4001),
        'a': range(1, 4001),
        's': range(1, 4001)
    })
    print(answer)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
