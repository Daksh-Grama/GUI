from tkinter import*
from tkinter import ttk
tk = Tk()
tk.title("Multiplication Tables")

tk.geometry("400x500")

a = ttk.Combobox(tk, values = [i for i in range(1, 101)])
a.place(x = 25, y = 100)
a.current(0)

b = Label(tk, text = "Choose a Number").place(x = 25, y = 50)

c = Label(tk, text = "Choose up to times").place(x = 200, y = 50)

x_var = StringVar()
d = ttk.Radiobutton(tk, text = "10", variable = x_var, value = "10")
d.place(x = 250, y = 100)

e = ttk.Radiobutton(tk, text = "20", variable = x_var, value = "20")
e.place(x = 250, y = 125)

f = ttk.Radiobutton(tk, text = "30", variable = x_var, value = "30")
f.place(x = 250, y = 150)

# g = Text(tk, x = 150, y = 100).place(x = 1, y = 200)
# def TimesTable ():
#     Number = int(a.get())
#     Times = int(x_var.get())
#     j = ""
#     for k in range (1, Times):
#         for l in range(Number):
#             print(f"{Times} x {Number} = {Times * Number}")
g = Text(tk,x = 150, y = 100)
g.place(x=1, y=200)

def TimesTable():
    Number = int(a.get())
    Times = int(x_var.get())
    
    g.delete("1.0", "end")  # Clear previous results
    
    for k in range(1, Times + 1):
        result = f"{Number} x {k} = {Number * k}\n"
        g.insert("end", result)



h = Button(tk, text = "Generate Table", command = TimesTable).place(x = 100, y = 160)


















tk.mainloop()