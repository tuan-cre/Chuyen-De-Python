from tkinter import *

def input(n):
    stringA.set(n)
    return

def cong(n):
    stringA.set(n)
    return

root = Tk()
frameButton = Frame(root)
frameButton2 = Frame(root)
frameButton3 = Frame(root)
root.minsize(height=250, width=200)
root.maxsize(height=250, width=200)
stringA = StringVar()
Entry(root, width=32, textvariable=stringA).grid(row=0, column=0)
Button(frameButton, text="1", width=8, command=input(1)).grid(row=1, column=0)
Button(frameButton, text="2", width=8, command=input(2)).grid(row=1, column=1)
Button(frameButton, text="3", width=8, command=root.quit).grid(row=1, column=2)
Button(frameButton, text="4", width=8, command=root.quit).grid(row=2, column=0)
Button(frameButton, text="5", width=8, command=root.quit).grid(row=2, column=1)
Button(frameButton, text="6", width=8, command=root.quit).grid(row=2, column=2)
Button(frameButton, text="7", width=8, command=root.quit).grid(row=3, column=0)
Button(frameButton, text="8", width=8, command=root.quit).grid(row=3, column=1)
Button(frameButton, text="9", width=8, command=root.quit).grid(row=3, column=2)
Button(frameButton, text="-", width=8, command=root.quit).grid(row=4, column=0)
Button(frameButton, text="0", width=8, command=root.quit).grid(row=4, column=1)
Button(frameButton, text=".", width=8, command=root.quit).grid(row=4, column=2)
Button(frameButton2, text="+", width=4, command=root.quit).grid(row=5, column=0)
Button(frameButton2, text="-", width=4, command=root.quit).grid(row=5, column=1)
Button(frameButton2, text="*", width=4, command=root.quit).grid(row=5, column=2)
Button(frameButton2, text="/", width=4, command=root.quit).grid(row=5, column=3)
Button(frameButton2, text="=", width=4, command=root.quit).grid(row=5, column=4)
frameButton.grid(row=1, column=0, columnspan=3)
frameButton2.grid(row=5, column=0, columnspan=3)
frameButton3.grid(row=6, column=0, columnspan=3)

Button(frameButton3, text="Clr", width=25, command=root.quit).grid(row=6, column=0)

root.mainloop()