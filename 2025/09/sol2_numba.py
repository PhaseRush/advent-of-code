import timeit
import itertools
from numba import jit
import numpy as np

with open("2025/09/test.txt") as f:
    lines = f.read().splitlines()
    coords = [tuple(map(int, x.split(","))) for x in lines]
    l = coords + [coords[0]]
    # Precompute line segments for faster access
    line_segments = list(itertools.pairwise(l))

    # Precompute normalized line segments (avoid repeated normalization)
    normalized_segments = []
    for (lx1, ly1), (lx2, ly2) in line_segments:
        lx_min, lx_max = (lx1, lx2) if lx1 <= lx2 else (lx2, lx1)
        ly_min, ly_max = (ly1, ly2) if ly1 <= ly2 else (ly2, ly1)
        normalized_segments.append((lx_min, lx_max, ly_min, ly_max))

    # Convert to numpy arrays for Numba
    coords_array = np.array(coords, dtype=np.int32)
    segments_array = np.array(normalized_segments, dtype=np.int32)


def check_intersect(x1, y1, x2, y2):
    # Normalize rectangle coordinates once
    rx_min, rx_max = (x1, x2) if x1 <= x2 else (x2, x1)
    ry_min, ry_max = (y1, y2) if y1 <= y2 else (y2, y1)

    # Use precomputed normalized segments
    for lx_min, lx_max, ly_min, ly_max in normalized_segments:
        # Check if rectangles overlap (if they do, we reject)
        if not (lx_max <= rx_min or rx_max <= lx_min or
                ly_max <= ry_min or ry_max <= ly_min):
            return False
    return True


@jit(nopython=True)
def check_intersect_numba(x1, y1, x2, y2, segments):
    # Normalize rectangle coordinates
    rx_min = min(x1, x2)
    rx_max = max(x1, x2)
    ry_min = min(y1, y2)
    ry_max = max(y1, y2)

    # Check against all precomputed normalized segments
    for i in range(len(segments)):
        lx_min, lx_max, ly_min, ly_max = segments[i]
        # Check if rectangles overlap (if they do, we reject)
        if not (lx_max <= rx_min or rx_max <= lx_min or
                ly_max <= ry_min or ry_max <= ly_min):
            return False
    return True


def f():
    ans = 0
    # Generate all combinations with their areas
    combos_with_area = []
    for c1, c2 in itertools.combinations(coords, 2):
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        combos_with_area.append((area, x1, y1, x2, y2))

    # Sort by area descending - check largest first
    combos_with_area.sort(reverse=True)

    for area, x1, y1, x2, y2 in combos_with_area:
        # Early termination: if remaining areas can't beat current best, stop
        if area <= ans:
            break
        if check_intersect(x1, y1, x2, y2):
            ans = area

    print(f"ans {ans}")


def f2():
    """Numba-accelerated version."""
    ans = 0
    # Generate all combinations with their areas
    combos_with_area = []
    for c1, c2 in itertools.combinations(coords, 2):
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        combos_with_area.append((area, x1, y1, x2, y2))

    # Sort by area descending - check largest first
    combos_with_area.sort(reverse=True)

    for area, x1, y1, x2, y2 in combos_with_area:
        # Early termination
        if area <= ans:
            break
        if check_intersect_numba(x1, y1, x2, y2, segments_array):
            ans = area

    print(f"ans {ans}")


if __name__ == "__main__":
    iters = 1

    print("Running vanilla version (f):")
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")

    print("\nRunning Numba-accelerated version (f2):")
    # Warm up JIT
    f2()
    x2 = timeit.timeit(lambda: f2(), number=iters)
    print(f"{x2 / iters: 0.2f} s")
