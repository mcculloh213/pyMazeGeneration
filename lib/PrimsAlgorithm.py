import math
import random
from lib.node import Node

__author__ = "H.D. 'Chip' McCullough"


def generate_grid(height: int, width: int) -> list:
    grd = []
    for i in range(0, height):
        subList = []
        for j in range(0, width):
            n = Node()
            subList.append(n)
            if len(subList) > 1:
                n.west = subList[j-1]
                subList[j-1].east = n
        grd.append(subList)
        if len(grd) > 1:
            for cn in grd[i]:
                cn.north = grd[i-1][grd[i].index(cn)]
                grd[i-1][grd[i].index(cn)].south = cn

    return grd


def mark(grid: list, fringe: list = None):
    if fringe is not None:
        n = random.choice(fringe)
        n.visited = 1
    else:
        subList = random.choice(grid)
        n = random.choice(subList)
        n.visited = 1


def generate_fringe(grid: list) -> list:
    mrk = []
    fng = []
    for row in grid:
        for n in row:
            if n.visited == 1:
                mrk.append(n)

    for n in mrk:
        if n.north is not None and n.north.visited == 0 and n.north not in fng:
            fng.append(n.north)
        if n.south is not None and n.south.visited == 0 and n.south not in fng:
            fng.append(n.south)
        if n.east is not None and n.east.visited == 0 and n.east not in fng:
            fng.append(n.east)
        if n.west is not None and n.west.visited == 0 and n.west not in fng:
            fng.append(n.west)

    return fng


def print_grid(grid: list):
    for row in grid:
        for n in row:
            print(n, end=" ")
        print("")


def model(grid: list, height: int, width: int) -> list:
    nX = (2 * width) + 1
    nY = (2 * height) + 1
    mat = []
    for r in range(0, nY):
        vec = []
        for c in range(0, nX):
            if r == 0 or r == (nY - 1) or c == 0 or c == (nX - 1):
                vec.append(0)
            else:
                nR = math.floor((r - 1) / 2)
                nC = math.floor((c - 1) / 2)
                if grid[nR][nC].visited == 1 and c % 2 == 1 and r % 2 == 1:
                    vec.append(1)
                else:
                    vec.append(-1)
        mat.append(vec)

    return mat

# if __name__ == "__main__":
#     marked = 0
#     g = generate_grid(3, 3)
#     print_grid(g)
#     print()
#     mark(g)
#     print_grid(g)
#     print()
#     marked += 1
#     while (marked < 3 * 3):
#         fr = generate_fringe(g)
#         mark(g, fr)
#         print_grid(g)
#         print()
#         marked += 1
