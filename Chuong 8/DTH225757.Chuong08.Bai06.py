from tkinter import *

root = Tk()
root.title("frame 2")

Label(root, text = "borderwidth = 0").grid(row = 0, column=0)
Button(root, text = "raised", width=10,borderwidth = 0, relief = RAISED).grid(row = 0, column=1)
Button(root, text = "sunken", width=10,borderwidth = 0, relief = SUNKEN).grid(row = 0, column=2)
Button(root, text = "flat", width=10,borderwidth = 0, relief = FLAT).grid(row = 0, column=3)
Button(root, text = "ridge", width=10,borderwidth = 0, relief = RIDGE).grid(row = 0, column=5)
Button(root, text = "groove", width=10,borderwidth = 0, relief = GROOVE).grid(row = 0, column=4)
Button(root, text = "solid", width=10,borderwidth = 0, relief = SOLID).grid(row = 0, column=6)
Label(root, text = "borderwidth = 1").grid(row = 1, column=0)
Button(root, text = "raised", width=10,borderwidth = 1, relief = RAISED).grid(row = 1, column=1)
Button(root, text = "sunken", width=10,borderwidth = 1, relief = SUNKEN).grid(row = 1, column=2)
Button(root, text = "flat", width=10,borderwidth = 1, relief = FLAT).grid(row = 1, column=3)
Button(root, text = "ridge", width=10,borderwidth = 1, relief = RIDGE).grid(row = 1, column=5)
Button(root, text = "groove", width=10,borderwidth = 1, relief = GROOVE).grid(row = 1, column=4)
Button(root, text = "solid", width=10,borderwidth = 1, relief = SOLID).grid(row = 1, column=6)
Label(root, text = "borderwidth = 2").grid(row = 2, column=0)
Button(root, text = "raised", width=10,borderwidth = 2, relief = RAISED).grid(row = 2, column=1)
Button(root, text = "sunken", width=10,borderwidth = 2, relief = SUNKEN).grid(row = 2, column=2)
Button(root, text = "flat", width=10,borderwidth = 2, relief = FLAT).grid(row = 2, column=3)
Button(root, text = "ridge", width=10,borderwidth = 2, relief = RIDGE).grid(row = 2, column=5)
Button(root, text = "groove", width=10,borderwidth = 2, relief = GROOVE).grid(row = 2, column=4)
Button(root, text = "solid", width=10,borderwidth = 2, relief = SOLID).grid(row = 2, column=6)
Label(root, text = "borderwidth = 3").grid(row = 3, column=0)
Button(root, text = "raised", width=10,borderwidth = 3, relief = RAISED).grid(row = 3, column=1)
Button(root, text = "sunken", width=10,borderwidth = 3, relief = SUNKEN).grid(row = 3, column=2)
Button(root, text = "flat", width=10,borderwidth = 3, relief = FLAT).grid(row = 3, column=3)
Button(root, text = "ridge", width=10,borderwidth = 3, relief = RIDGE).grid(row = 3, column=5)
Button(root, text = "groove", width=10,borderwidth = 3, relief = GROOVE).grid(row = 3, column=4)
Button(root, text = "solid", width=10,borderwidth = 3, relief = SOLID).grid(row = 3, column=6)
Label(root, text = "borderwidth = 4").grid(row = 4, column=0)
Button(root, text = "raised", width=10,borderwidth = 4, relief = RAISED).grid(row = 4, column=1)
Button(root, text = "sunken", width=10,borderwidth = 4, relief = SUNKEN).grid(row = 4, column=2)
Button(root, text = "flat", width=10,borderwidth = 4, relief = FLAT).grid(row = 4, column=3)
Button(root, text = "ridge", width=10,borderwidth = 4, relief = RIDGE).grid(row = 4, column=5)
Button(root, text = "groove", width=10,borderwidth = 4, relief = GROOVE).grid(row = 4, column=4)
Button(root, text= "solid" , width=10,borderwidth = 4, relief = SOLID).grid(row = 4, column=6)

root.mainloop()
