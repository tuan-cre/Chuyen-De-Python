from tkinter import Tk, StringVar, Label, Entry, Button

root = Tk()
root.minsize(300, 300)

doF = StringVar()

def chuyendoFsangdoC():
    try:
        fahrenheit = float(doF.get())
        celsius = (fahrenheit - 32) * 5 / 9
        ketqua.config(text=f"{celsius:.2f} °C")
    except ValueError:
        ketqua.config(text="Invalid input")

Label(root, text="Nhập độ F").grid(row=0, column=0)
Entry(root, width=20, textvariable=doF).grid(row=0, column=1)

ketqua = Label(root, text="")
ketqua.grid(row=2, column=1)

Button(root, text="Chuyển", command=chuyendoFsangdoC).grid(row=1, column=1)
Label(root, text="Độ C").grid(row=2, column=0)

root.mainloop()
