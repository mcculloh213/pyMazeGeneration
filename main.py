import tkinter

if __name__ == "__main__":
    root = tkinter.Tk()
    for rows in range(0, 20):
        for cols in range(0, 20):
            # tkinter.Label(root, text="{0},{1}".format(rows, cols), borderwidth=2).grid(row=rows, column=cols)
            tkinter.Canvas(root, bd=3, bg="white", height=10, width=10).grid(row=rows, column=cols)
    root.mainloop()
