import time

with open('input.txt') as f:
    lines = f.read().splitlines()

    start = time.process_time_ns()

    dirs = list(lines[0])

    map = {}
    for l in lines[2:]:
        key, choices = l.split("=")
        choices = choices.replace('(', '').replace(')', '').strip().split(", ")
        map[key.strip()] = (choices[0], choices[1])

    # print(map)

    iters = 0
    next_pos = 'AAA'
    while True:
        if next_pos == 'ZZZ':
            break
        for d in dirs:
            if d == 'R':
                next_pos = map[next_pos][1]
            else:
                next_pos = map[next_pos][0]
            iters += 1

    print(iters)

    print((time.process_time_ns() - start) / 10e6, " ms")
