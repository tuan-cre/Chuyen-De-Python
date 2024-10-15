# Phần mềm tính BMI

from tkinter import *

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height / 100) ** 2
        bmi_result.set(f"{bmi:.2f}")
        
        if bmi < 18.5:
            status.set("Gầy")
            risk.set("Thấp")
        elif 18.5 <= bmi < 24.9:
            status.set("Bình thường")
            risk.set("Trung bình")
        elif 25 <= bmi < 29.9:
            status.set("Thừa cân")
            risk.set("Tăng")
        else:
            status.set("Béo phì")
            risk.set("Cao")
    except ValueError:
        bmi_result.set("Dữ liệu không hợp lệ")
        status.set("")
        risk.set("")

root = Tk()
root.configure(borderwidth=1, background="yellow")
root.minsize(height=500, width=300)
root.title("Máy tính BMI")

bmi_result = StringVar()
status = StringVar()
risk = StringVar()

Label(root, text="Nhập chiều cao (cm): ", font=("consolas", 10), background="yellow", anchor=W).grid(row=0, column=0, padx=10, pady=10, sticky=W)
height_entry = Entry(root, width=20)
height_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Nhập cân nặng (kg): ", font=("consolas", 10), background="yellow", anchor=W).grid(row=1, column=0, padx=10, pady=10, sticky=W)
weight_entry = Entry(root, width=20)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

Button(root, text="Tính BMI", font=("consolas", 10), command=calculate_bmi, background="blue", foreground="white").grid(row=2, column=1, columnspan=2, pady=10)

Label(root, text="BMI của bạn: ", font=("consolas", 10), background="yellow", anchor=W).grid(row=3, column=0, padx=10, pady=10, sticky=W)
Entry(root, textvariable=bmi_result, width=20, state='readonly').grid(row=3, column=1, padx=10, pady=10)

Label(root, text="Tình trạng của bạn: ", font=("consolas", 10), background="yellow", anchor=W).grid(row=4, column=0, padx=10, pady=10, sticky=W)
Entry(root, textvariable=status, width=20, state='readonly').grid(row=4, column=1, padx=10, pady=10)

Label(root, text="Nguy cơ phát triển bệnh: ", font=("consolas", 10), background="yellow", anchor=W).grid(row=5, column=0, padx=10, pady=10, sticky=W)
Entry(root, textvariable=risk, width=20, state='readonly').grid(row=5, column=1, padx=10, pady=10)

Button(root, text="Thoát", font=("consolas", 10), command=root.quit, background="blue", foreground="white").grid(row=6, column=1, pady=10)

root.mainloop()