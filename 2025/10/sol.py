import timeit
from collections import deque

with open('2025/10/test.txt') as f:
    lines = [x.split() for x in f.read().splitlines()]
    all_lights = [list(map(lambda i: i == "#", x[0][1:-1])) for x in lines]
    # all_buttons = [x[1:-1] for x in lines]
    all_buttons = [[list(map(int, y.strip("()").split(","))) for y in x[1:-1]] for x in lines]
    all_jolts = [x[-1] for x in lines]
    # print(all_lights, all_buttons, all_jolts)
    # lines = [list(row) for row in lines]


def solve(current_lights, target_lights, buttons):
    q = deque(((current_lights, 0),))
    visited = set(tuple(current_lights))

    while q:
        curr_lights, moves = q.popleft()

        if curr_lights == target_lights:
            return moves
        
        for button in buttons:
            new_lights = curr_lights[:]
            for b in button:
                new_lights[b] = not new_lights[b]
            
            if tuple(new_lights) not in visited:
                visited.add(tuple(new_lights))
                q.append((new_lights, moves + 1))
    
    return 0

def f():
    ans = 0

    for idx in range(len(lines)):
        lights = all_lights[idx]
        buttons = all_buttons[idx]
        ans += solve([False] * len(lights), lights, buttons)

    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
