import tkinter
from lib.PrimsAlgorithm import *

HEIGHT = 10
PX_HEIGHT = 10
WIDTH = 10
PX_WIDTH = 10
MARKED = 0

if __name__ == "__main__":
    root = tkinter.Tk()
    g = generate_grid(HEIGHT, WIDTH)
    mark(g)
    MARKED += 1
    while MARKED < HEIGHT * WIDTH:
        fr = generate_fringe(g)
        mark(g, fr)
        MARKED += 1
    print_grid(g)
    mat = model(g, HEIGHT, WIDTH)
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] == 0:
                tkinter.Canvas(root, bd=0, highlightthickness=0, bg='black',
                               height=PX_HEIGHT, width=PX_WIDTH).grid(row=i, column=j)
            elif mat[i][j] == 1:
                tkinter.Canvas(root, bd=0, highlightthickness=0, bg='white',
                               height=PX_HEIGHT, width=PX_WIDTH).grid(row=i, column=j)
            else:
                tkinter.Canvas(root, bd=0, highlightthickness=0, bg='blue',
                               height=PX_HEIGHT, width=PX_WIDTH).grid(row=i, column=j)

    root.mainloop()