import timeit

with open('2025/06/test.txt') as f:
    lines = [x.strip() for x in f.read().splitlines()]
    Y = len(lines) -1  # don't count operators
    X = len(lines[0].split())
    nums = []
    for row in lines[0:len(lines)-1]:
        nums.append([int(x) for x in row.split()])
    operators = lines[-1].strip().split()

    # print(nums)
    # print(operators)

def f():
    import math
    ans = 0
    for x in range(X):
        curr_op = operators[x]
        curr_nums = []
        for y in range(Y):
            curr_nums.append(nums[y][x])
            if curr_op == "+":
                ans += sum(curr_nums)
            else: # multiply
                ans += math.prod(curr_nums)

    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
