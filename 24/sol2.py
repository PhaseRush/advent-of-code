import math
import timeit

import z3
from euclid import *
from z3 import *

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


def f():
    # yoinked this to learn z3
    solver = z3.Solver()
    px, py, pz, vx, vy, vz = [z3.Int(var) for var in ["x", "y", "z", "vx", "vy", "vz"]]

    for idx in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = parsed[idx]

        t = z3.Int(f"t{idx}")
        solver.add(t >= 0)
        solver.add(px + vx * t == cpx + cvx * t)
        solver.add(py + vy * t == cpy + cvy * t)
        solver.add(pz + vz * t == cpz + cvz * t)

    solver.check()
    model = solver.model()
    (px, py, pz) = (model.eval(px), model.eval(py), model.eval(pz))
    print(px.as_long() + py.as_long() + pz.as_long())


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
