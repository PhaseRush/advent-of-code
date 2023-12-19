import timeit
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def all(self):
        return self.x + self.m + self.a + self.s


with open('test.txt') as f:
    lines = f.read().splitlines()
    empty = lines.index("")
    wfs_lines = lines[0:empty]
    wfs = defaultdict(list)
    for wf in wfs_lines:
        name, details = wf.split("{")
        details = details[:-1].split(",")
        wfs[name] = details

    parts_lines = [x[1:-1] for x in lines[empty + 1:]]
    parts = []
    for part in parts_lines:
        spl = part.split(",")
        x = int(spl[0][2:])
        m = int(spl[1][2:])
        a = int(spl[2][2:])
        s = int(spl[3][2:])
        parts.append(Part(x, m, a, s))


def test(part, wf):  # -> pass, fail, or next wf
    for test in wf:
        if ":" in test:
            colon = test.index(':')
        else:
            return test

        param = test[0]
        cond = test[1]
        amount = test[2:colon]
        next_step = test[colon + 1:]
        test_str = f"part.{test[:colon]}"
        res = eval(test_str)
        if res:
            return next_step

    return "R"


def f():
    passers = []
    ans = 0
    rejects = []
    test(parts[0], wfs['in'])

    for part in parts:
        curr_wf = wfs['in']
        while True:
            result = test(part, curr_wf)
            if result == 'A':
                passers.append(part)
                ans += part.all()
                break
            elif result == 'R':
                rejects.append(part)
                break
            else:
                curr_wf = wfs[result]

    print(ans)


print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
