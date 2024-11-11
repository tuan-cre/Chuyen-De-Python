from tkinter import Tk, StringVar, Label, Entry, Button

root = Tk()
root.minsize(300, 300)

nam = StringVar()

def chuyenNamDuongLichSangAmLich():
    year = int(nam.get())
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    can_index = year % 10
    chi_index = year % 12
    am_lich = f"{can[can_index]} {chi[chi_index]}"
    ketqua.config(text=am_lich)

Label(root, text="Nhập năm dương:").grid(row=0, column=0)
Entry(root, width=20, textvariable=nam).grid(row=0, column=1)

ketqua = Label(root, text="")
ketqua.grid(row=2, column=1)

Button(root, text="Chuyển", command=chuyenNamDuongLichSangAmLich).grid(row=1, column=1)
Label(root, text="Năm âm:").grid(row=2, column=0)

root.mainloop()
