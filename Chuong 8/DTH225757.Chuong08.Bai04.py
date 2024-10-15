from tkinter import *

def input_number(n):
    current = value.get()
    value.set(current + str(n))

def clear():
    value.set("")

def calculate():
    try:
        result = eval(value.get())
        value.set(result)
    except Exception as e:
        value.set("Error")

root = Tk()
root.configure(borderwidth=1, background="light blue")
frameButton = Frame(root)
frameButton2 = Frame(root)
frameButton3 = Frame(root)
# root.minsize(height=250, width=200)
root.maxsize(height=300, width=200)

value = StringVar()
Entry(root, width=32, textvariable=value).grid(row=0, column=0)
Button(frameButton, text="1", width=8, command=lambda: input_number(1)).grid(row=1, column=0)
Button(frameButton, text="2", width=8, command=lambda: input_number(2)).grid(row=1, column=1)
Button(frameButton, text="3", width=8, command=lambda: input_number(3)).grid(row=1, column=2)
Button(frameButton, text="4", width=8, command=lambda: input_number(4)).grid(row=2, column=0)
Button(frameButton, text="5", width=8, command=lambda: input_number(5)).grid(row=2, column=1)
Button(frameButton, text="6", width=8, command=lambda: input_number(6)).grid(row=2, column=2)
Button(frameButton, text="7", width=8, command=lambda: input_number(7)).grid(row=3, column=0)
Button(frameButton, text="8", width=8, command=lambda: input_number(8)).grid(row=3, column=1)
Button(frameButton, text="9", width=8, command=lambda: input_number(9)).grid(row=3, column=2)
Button(frameButton, text="0", width=8, command=lambda: input_number(0)).grid(row=4, column=1)
Button(frameButton, text=".", width=8, command=lambda: input_number('.')).grid(row=4, column=2)
Button(frameButton, text="-", width=8, command=lambda: input_number('-')).grid(row=4, column=0)
Button(frameButton2, text="+", width=4, command=lambda: input_number('+')).grid(row=5, column=0)
Button(frameButton2, text="-", width=4, command=lambda: input_number('-')).grid(row=5, column=1)
Button(frameButton2, text="*", width=4, command=lambda: input_number('*')).grid(row=5, column=2)
Button(frameButton2, text="/", width=4, command=lambda: input_number('/')).grid(row=5, column=3)
Button(frameButton2, text="=", width=5, command=calculate).grid(row=5, column=4)
frameButton.grid(row=1, column=0, columnspan=3)
frameButton2.grid(row=5, column=0, columnspan=3)
frameButton3.grid(row=6, column=0, columnspan=3)

Button(frameButton3, text="Clr", width=27, command=clear).grid(row=6, column=0)

root.mainloop()