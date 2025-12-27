from tkinter import*
from tkinter import ttk
import tkinter as tk
tk = Tk()
tk.geometry("600x300")
tk.title("Pizza Hut Order Page")
tk.config(bg = "black")
Pizza1 = Label(tk, highlightbackground = "black", text = "What pizza would you like?") 
Pizza1.place(y = 50, x = 50)

Pizza2 = Label(tk, highlightbackground = "black", text = "Select the quantity")
Pizza2.place(y = 100, x = 50)

Pizza3 = Label(tk, highlightbackground = "black", text = "Welcome to Pizza Hut")
Pizza3.place(y = 10, x = 250)

Pizza4 = ["Veggie", "Peperoni", "Four Cheese", "Green Power", "Little Italy"]

Pizza5 = StringVar()

Pizza6 = ttk.Combobox(tk, textvariable= Pizza5, values = Pizza4)
Pizza6.place(x = 225, y = 50)
Pizza6.current(0)


Pizza7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Pizza8 = StringVar()

Pizza9 = ttk.Combobox(tk, textvariable= Pizza8, values = Pizza7)
Pizza9.place(x = 225, y = 100)
Pizza9.current(0)

Pizza10 = StringVar(value = "Medium")

Pizza11 = [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]

Pizza = 50

for text, size in Pizza11:
    Pizza12 = ttk.Radiobutton(tk, text = text, variable = Pizza10, value = size)
    Pizza12.place(x = 450, y = Pizza )
    
    Pizza = Pizza + 40
    
def onclick():
    Quantity = Pizza8.get()
    pizza = Pizza6.get()
    Size = Pizza10.get()
    Alpha = Label(tk, text="")
    Alpha.place(x = 150, y = 200)

    Alpha.config(text = f"You have ordered {Quantity} {Size} {pizza}")
    


Pizza13 = Button(tk, text = "Submit Order", borderwidth = 0, highlightbackground = "black", command = onclick)
Pizza13.place(y = 150, x = 200)



tk.mainloop()