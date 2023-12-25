import math
import timeit
from euclid import *

with (open('input.txt') as f):
    lines = [line.split(" @ ") for line in f.read().splitlines()]
    parsed = []
    for pos, vel in lines:
        px, py, pz = pos.split(", ")
        vx, vy, vz = vel.split(", ")
        parsed.append(((int(px), int(py), int(pz)), (int(vx), int(vy), int(vz))))
    # x_min, y_min = 7, 7
    # x_max, y_max = 27, 27
    x_min, y_min = 200000000000000, 200000000000000
    x_max, y_max = 400000000000000, 400000000000000


    rays = []
    for pos, vel in parsed:
        # rays.append(Ray3(Point3(), Vector3()))
        rays.append(Ray2(Point2(pos[0], pos[1]), Vector2(vel[0], vel[1])))


def dist(a, b, z=False):
    if z:
        return math.sqrt((a[0][0] - b[0][0]) ** 2 + (a[0][1] - b[0][1]) ** 2 + (a[0][2] - b[0][2]) ** 2)
    else:
        return math.sqrt((a[0][0] - b[0][0]) ** 2 + (a[0][1] - b[0][1]) ** 2)


def move(a):
    return a[0][0] + a[1][0], a[0][1] + a[1][1], a[0][2] + a[1][2]


def check_within(point: Point2):
    return x_min < point.x < x_max and y_min < point.y < y_max
    # return x_min <= point.x <= x_max and y_min <= point.y <= y_max

def check(a: Line2, b: Line2):
    intersect = a.intersect(b)
    if intersect:
        return check_within(intersect)
    else:
        return False

def f():
    count = 0
    intersects = []
    for r1_idx, r1 in enumerate(rays):
        for r2_idx in range(r1_idx + 1, len(rays)):
            r2 = rays[r2_idx]
            if check(r1, r2):
                count += 1
                intersects.append((r1, r2))
    print(intersects)
    print(count)

# print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
