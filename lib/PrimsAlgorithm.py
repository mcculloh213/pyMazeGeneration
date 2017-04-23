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


def mark(grid: list, order: list, fringe: list = None):
    if fringe is not None:
        n = random.choice(fringe)
        n.degree += 1
    else:
        subList = random.choice(grid)
        n = random.choice(subList)

    n.visited = 1
    order.append(n)


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


def model(grid: list, order: list, height: int, width: int) -> list:
    nX = (2 * width) + 1
    nY = (2 * height) + 1
    mat = []

    for r in range(0, nY):
        vec = []
        for c in range(0, nX):
            if r == 0 or r == (nY - 1) or c == 0 or c == (nX - 1):
                vec.append(0)
            else:
                nR = int(math.floor((r - 1) / 2))
                nC = int(math.floor((c - 1) / 2))
                if grid[nR][nC].visited == 1 and c % 2 == 1 and r % 2 == 1:
                    vec.append(1)
                else:
                    vec.append(0)
        mat.append(vec)

    edges = 0
    while len(order) > 1:
        n1 = order.pop()
        order.reverse()
        for n in order:
            p1 = (-1, -1)
            p2 = (-1, -1)
            for r in range(0, len(grid)):
                for c in range(0, len(grid[r])):
                    if n1 is grid[r][c]:
                        p1 = ((2 * r) + 1, (2 * c) + 1)
                    if n is grid[r][c]:
                        p2 = ((2 * r) + 1, (2 * c) + 1)
            if abs((p2[0] - p1[0]) / 2) == 1 and abs((p2[1] - p1[1]) / 2) == 0:
                if n1.isNorthOf(n):
                    mat[p1[0] + 1][p1[1]] = 1
                elif n1.isSouthOf(n):
                    mat[p2[0] + 1][p2[1]] = 1
                else:
                    print("Uh oh")
                break
            elif abs((p2[1] - p1[1]) / 2) == 1 and abs((p2[0] - p1[0]) / 2) == 0:
                if n1.isEastOf(n):
                    mat[p2[0]][p2[1] + 1] = 1
                elif n1.isWestOf(n):
                    mat[p2[0]][p2[1] - 1] = 1
                else:
                    print("Uh oh.")
                break
            else:
                continue
        order.reverse()

    return mat
