import timeit

with open('2025/01/test.txt') as f:
    lines = f.read().splitlines()
    print(lines)

def f():
    pos = 50
    ans = 0
    for l in lines:
        dir, rotation = l[0], int(l[1:])
        for i in range(rotation):
            if dir == "R":
                pos += 1
                if pos % 100 == 0:
                    ans += 1
            else:
                pos -= 1
                if pos % 100 == 0:
                    ans += 1
    
    print(ans)


def f2():
    pos = 50
    ans = 0
    for l in lines:
        dir, rotation = l[0], int(l[1:])
        num_rotations = rotation // 100
        leftover = rotation % 100
        dir = -1 if dir == "L" else 1
    
        pos += dir * leftover

        count_current_rot = (pos <= 0 or pos >= 100) and ((pos - dir * rotation) % 100 > 0)
        ans += num_rotations + count_current_rot

        pos %= 100
    
    print(ans)

def f3():
    pos = 50
    ans = 0
    prev_dir = "R"
    for l in lines:
        dir, rotation = l[0], int(l[1:])
        if dir != prev_dir:
            pos = 100 - pos
            prev_dir = dir
        
        pos = (pos % 100) + rotation
        ans += pos // 100
    
    print(ans)



if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
