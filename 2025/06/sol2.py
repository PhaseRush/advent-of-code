import timeit

with open('2025/06/test.txt') as f:
    lines = f.read().splitlines()
    Y = len(lines) -1  # don't count operators
    X = len(lines[0].split())
    nums = []
    for row in lines[0:len(lines)-1]:
        nums.append([int(x) for x in row.split()])
    operators = lines[-1]

def f():
    import math, re
    ans = 0

    pattern = re.compile(r"([+|*]\s+)")
    for a in re.finditer(pattern, operators):
        curr_nums = []
        curr_op = operators[a.start()]
        for x in range(a.start(), a.end()):
            curr_num = ""
            for y in range(Y):
                curr_char = lines[y][x]
                if (curr_char.isalnum()):
                    curr_num += curr_char
            if curr_num:
                curr_nums.append(int(curr_num))

        if curr_op == "*":
            ans += math.prod(curr_nums)
        else:
            ans += sum(curr_nums)

    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
