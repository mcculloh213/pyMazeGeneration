import tkinter

PX_HEIGHT = 10
PX_WIDTH = 10
BG_PASSED="#bb0000"

def depth_first_search(maze: list, root: tkinter.Tk = None):
    """
    Depth first search maze solver
    :param maze: (n x m) Maze matrix model
    :type maze: list
    :param root: Root GUI view
    :type root: tkinter.Tk
    """
    discovered = []
    stack = []
    start = (-1, -1)

    for i in range(0, len(maze)):
        if maze[i][0] != 0:
            start = (i, 0)
            break
    if start == (-1, -1):
        for j in range(0, len(maze[0])):
            if maze[0][j] != 0:
                start = (0, j)
                break

    print("Start found at: {0}".format(start))

    stack.append(start)

    while len(stack) > 0:
        loc = stack.pop()

        if root is not None:
            if len(discovered) > 0:
                tkinter.Canvas(root, bd=0, highlightthickness=0, bg=BG_PASSED,
                                height=PX_HEIGHT, width=PX_WIDTH).grid(row=discovered[-1][0], column=discovered[-1][1])
            tkinter.Canvas(root, bd=0, highlightthickness=0, bg='red',
                           height=PX_HEIGHT, width=PX_WIDTH).grid(row=loc[0], column=loc[1])
            root.update()

        if (len(maze) -1 in loc) or (len(maze[0]) - 1 in loc):
            break

        discovered.append(loc)

        north = (loc[0] - 1, loc[1])
        south = (loc[0] + 1, loc[1])
        east = (loc[0], loc[1] + 1)
        west = (loc[0], loc[1] - 1)

        if north[0] > 0 and north[0] < len(maze) and north[1] > 0 and north[1] < len(maze):
            if maze[north[0]][north[1]] != 0 and north not in discovered:
                stack.append(north)
        if south[0] > 0 and south[0] < len(maze) and south[1] > 0 and south[1] < len(maze):
            if maze[south[0]][south[1]] != 0 and south not in discovered:
                stack.append(south)
        if east[0] > 0 and east[0] < len(maze[0]) and east[1] > 0 and east[1] < len(maze[0]):
            if maze[east[0]][east[1]] != 0 and east not in discovered:
                stack.append(east)
        if west[0] > 0 and west[0] < len(maze[0]) and west[1] > 0 and west[1] < len(maze[0]):
            if maze[west[0]][west[1]] != 0 and west not in discovered:
                stack.append(west)
