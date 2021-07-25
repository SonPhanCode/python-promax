from tkinter import *
tk = Tk()
tk.title("form test")
lb1 = Label(tk, text="đây là dòng chữ", font=(100),bg = "red")
lb1.pack()
btn = Button(tk,text ="click",bg = "blue")
btn.pack()
tk.mainloop()