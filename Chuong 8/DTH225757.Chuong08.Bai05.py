from tkinter import *

root = Tk()
root.title("Enter New Password")
Label(root, text="Old Password:").grid(row=0, column=0)
Entry(root, show="*").grid(row=0, column=1)
Label(root, text="New Password:").grid(row=1, column=0)
Entry(root, show="*").grid(row=1, column=1)
Label(root, text="Enter New Password Again:").grid(row=2, column=0)
Entry(root, show="*").grid(row=2, column=1)
frameButton = Frame()
Button(frameButton, text="OK").pack(side=LEFT)
Button(frameButton, text="Cancel").pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

root.mainloop()