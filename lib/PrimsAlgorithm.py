import random
from lib.node import Node

__author__ = "H.D. 'Chip' McCullough"


def grid(height: int, width: int) -> list:
    grid = []
    for i in range(0, height):
        subList = []
        for j in range(0, width):
            n = Node()
            subList.append(n)
            if len(subList) > 1:
                n.west = subList[j-1]
                subList[j-1].east = n
        grid.append(subList)
        if len(grid) > 1:
            for cn in grid[i]:
                cn.north = grid[i-1][grid[i].index(cn)]
                grid[i-1][grid[i].index(cn)].south = cn

    return grid


def mark(grid: list, fringe: list = None):
    if fringe is not None:
        n = random.choice(fringe)
        n.visited = 1
    else:
        subList = random.choice(grid)
        n = random.choice(subList)
        n.visited = 1


def fringe(grid: list) -> list:
    marked = []
    fringe = []
    for row in grid:
        for n in row:
            if n.visited == 1:
                marked.append(n)

    for n in marked:
        if n.north is not None and n.north.visited == 0 and n.north not in fringe:
            fringe.append(n.north)
        if n.south is not None and n.south.visited == 0 and n.south not in fringe:
            fringe.append(n.south)
        if n.east is not None and n.east.visited == 0 and n.east not in fringe:
            fringe.append(n.east)
        if n.west is not None and n.west.visited == 0 and n.west not in fringe:
            fringe.append(n.west)

    return fringe

def print_grid(grid: list):
    for row in grid:
        for n in row:
            print(n, end=" ")
        print("")

if __name__ == "__main__":
    marked = 0
    g = grid(20, 20)
    print_grid(g)
    print()
    mark(g)
    print_grid(g)
    print()
    marked += 1
    while (marked < 20 * 20):
        fr = fringe(g)
        mark(g, fr)
        print_grid(g)
        print()
        marked += 1
