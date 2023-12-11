import math
import time

with open('input.txt') as f:
    lines = f.read().splitlines()
    start = time.process_time_ns()
    dirs = list(lines[0])

    map = {}
    starts = []

    for l in lines[2:]:
        key, choices = l.split("=")
        choices = choices.replace('(', '').replace(')', '').strip().split(", ")
        map[key.strip()] = (choices[0], choices[1])
        if key.strip().endswith('A'):
            starts.append(key.strip())


    def find_iters(start):
        iters = 0
        next_pos = start
        while True:
            for d in dirs:
                if next_pos[2] == 'Z':
                    return iters
                if d == 'R':
                    next_pos = map[next_pos][1]
                else:
                    next_pos = map[next_pos][0]
                iters += 1


    end_iters = [find_iters(x) for x in starts]
    print(math.lcm(*end_iters))

    print((time.process_time_ns() - start) / 10e3, " us")
