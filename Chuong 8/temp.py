from tkinter import *


root = Tk()

Label(root, text="Artist Name").grid(row=0, column=0)   
Entry(root).grid(row=0, column=1)

root.mainloop()