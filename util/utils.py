# import numpy as np

def rotate_cw(m):
    rot = zip(*m[::-1])
    return [list(x) for x in rot]


def rotate_ccw(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]
