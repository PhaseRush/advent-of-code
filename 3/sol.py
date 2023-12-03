import re
import math

dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def check_symbol(input, to_check):
    for x, y in to_check:
        try:
            if input[y][x] not in ".0123456789":
                return True
        except:
            continue
    return False


if __name__ == '__main__':
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip())
    Y = len(input)
    X = len(input[0])
    nums = []
    for y in range(Y):
        for match in re.finditer(r"\d+", input[y]):
            curr = int(match.group(0))
            to_check = []
            for x in range(match.start(), match.end()):
                for dx, dy in dirs:
                    to_check.append((x + dx, y + dy))

            if check_symbol(input, to_check):
                nums.append(curr)

    print(nums)
    print(sum(nums))
    nums.clear()

    ## part 2

    gears = []
    for y in range(Y):
        for x in range(X):
            if input[y][x] == "*":
                gears.append((x, y))

    visited = set()
    for gx, gy in gears:
        gear_nums = []
        for dx, dy in dirs:
            if (gx + dx, gy + dy) in visited:
                continue
            visited.add((gx + dx, gy + dy))
            row = input[gy + dy]
            if row[gx + dx].isnumeric():
                curr_start = 0
                while row[gx + dx + curr_start].isnumeric():
                    visited.add((gx + dx + curr_start, gy + dy))
                    curr_start -= 1
                start = gx + dx + curr_start + 1
                curr_start = 1
                while start + curr_start < X and row[start + curr_start].isnumeric():
                    visited.add((start + curr_start, gy + dy))
                    curr_start += 1
                gear_nums.append(int(row[start:start + curr_start]))
        if len(gear_nums) == 2:
            nums.append(gear_nums[0] * gear_nums[1])

    print(sum(nums))
