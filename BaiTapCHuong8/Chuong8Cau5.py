'''
Câu 5: Màn hình đăng nhập
'''
from tkinter import*
from tkinter import messagebox
MATKHAUCU = "12345thanh"
def KTMK():
    try:
        mkcu = stringMKCU.get()
        mkmoi = stringMKMOI.get()
        xnmk = stringXNMK.get()
    except Exception:
        return
    
    if mkmoi == MATKHAUCU:
        messagebox.showerror("Lỗi", "Không được dùng mật khẩu cũ nha!")
        return
    
    if mkmoi != xnmk:
        messagebox.showerror("Lỗi", "Mật khẩu mới và xác nhận mật khẩu không khớp!")
        return
    
    if mkcu != MATKHAUCU:
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
        return
    
    stringMKCU.set("")
    stringMKMOI.set("")
    stringXNMK.set("")
    
root = Tk()
root.title("Enter new password")
root.minsize(height = 200, width = 350)

stringMKCU = StringVar()
stringMKMOI = StringVar()
stringXNMK = StringVar()

Label(root, text="Old password:", fg="pink").grid(row = 1, column =0)
Entry(root, width=25, textvariable=stringMKCU, show="*").grid(row =1, column=1)
Label(root, text="New password: ", fg="green").grid(row=2, column=0)
Entry(root, width=25, textvariable=stringMKMOI, show="*").grid(row=2, column =1)
Label(root, text="Enter new password again:",fg="red").grid(row=3, column =0)
Entry(root, width=25, textvariable= stringXNMK, show="*").grid(row=3, column = 1)

frameButton = Frame(root)
Button(frameButton, text= "Ok", command=KTMK ).pack(side= LEFT, padx = 10)
Button(frameButton, text="Cancel", command=root.quit).pack(side= LEFT, padx = 10)
frameButton.grid(row=4, columnspan=2, pady = 15)
root.mainloop()