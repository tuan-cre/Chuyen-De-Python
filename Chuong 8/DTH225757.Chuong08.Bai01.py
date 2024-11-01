# from tkinter import * 
 
# def tiepAction(): 
#     stringHSA.set("") 
#     stringHSB.set("") 
#     stringKQ.set("") 
 
# def giaiAction(): 
#     a=float(stringHSA.get()) 
#     b = float(stringHSB.get()) 
#     if a==0 and b ==0: 
#         stringKQ.set("Vô số nghiệm") 
#     elif a==0 and b!=0: 
#         stringKQ.set("Vô nghiệm") 
#     else: 
#         stringKQ.set("x="+str((-b/a))) 
   
# root=Tk() 
 
# stringHSA=StringVar() 
# stringHSB=StringVar() 
# stringKQ=StringVar() 
 
# root.title("PTB1-facebook.com/duythanhcse") 
# root.minsize(height=130,width=250) 
# root.resizable(height=True,width=True) 
 
# Label(root,text="Phương Trình Bậc 1",fg="red",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2) 
 
# Label(root,text="Hệ số a:").grid(row=1,column=0) 
# Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1) 
 
# Label(root,text="Hệ số b:").grid(row=2,column=0) 
# Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1) 
 
# frameButton=Frame() 
# Button(frameButton,text="Giải",command=giaiAction).pack(side=LEFT) 
# Button(frameButton,text="Tiếp",command=tiepAction).pack(side=LEFT) 
# Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT) 
# frameButton.grid(row=3,columnspan=2) 
 
# Label(root,text="Kết quả:").grid(row=4,column=0) 
# Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1) 
 
# root.mainloop()

from tkinter import *

root = Tk()
root.title("PTB1")
root.minsize(500, 500)

def giai():
    x = float(a.get())
    y = float(b.get())
    c.set((-y)/x)

def tiep():
    a.set("")
    b.set("")
    c.set("")

def thoat():
    root.quit()

a = StringVar()
b = StringVar()
c = StringVar()

Label(root, text="Phuong trinh bac I").grid(row=0, columnspan=2)
Label(root, text="He so a: ").grid(row=1, column=0)
Entry(root, textvariable=a).grid(row=1, column=1)

Label(root, text="He so b: ").grid(row=2, column=0)
Entry(root, textvariable=b).grid(row=2, column=1)

framebutton = Frame()
Button(framebutton, text="Giai", command=giai).pack(side=LEFT)
Button(framebutton, text="Tiep", command=tiep).pack(side=LEFT)
Button(framebutton, text="Thoat", command=thoat).pack(side=LEFT)
framebutton.grid(row=3, columnspan=2)

Label(root, text="Ket qua: ").grid(row=4, column=0)
Entry(root, textvariable=c).grid(row=4, column=1)

root.mainloop()