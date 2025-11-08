# from tkinter import*
# root = Tk()

# root.config(background = "light blue")
# TP = Listbox(root, width = 30, height = 30, bg = "dark blue").place(x = 250, y = 400)
# Title = Label(root, text = "Types of Birds", bg = "light blue", font = "All Rights Reserved 20 bold").place(x = 250, y = 450)
from tkinter import*

tk = Tk()
tk.geometry("150x100")
tk.title("Listbox")
scroll_bar = Scrollbar(tk)
scroll_bar.pack(side = RIGHT, fill = Y)
listbox = Listbox(tk, yscrollcommand = scroll_bar.set)
listbox.insert(0, "hi") 
listbox.insert(1, "hello")
# listbox.delete(0)
listbox.insert(2, "what are you doing ?")
listbox.insert(3, "welcome")
listbox.insert(4, "good morning")
listbox.insert(5, "good evening")
listbox.insert(6, "good night")
listbox.insert(7, "it is rainy")
listbox.insert(8, "are you okay ?")
listbox.insert(9, "what is that ?")
listbox.pack()


scroll_bar.config(command = listbox.yview)




tk.mainloop()