from tkinter import*

tk = Tk()
tk.geometry("300x300")
tk.title("Weight Converter")
Temperature = Label(tk, text = "Enter weight in Kilograms:").place(x = 75, y = 10)

Kilograms_Entry = Entry(tk)
Kilograms_Entry.place(x = 85, y = 50)

def onclick ():
    # print ("Entry Submitted!")
     Kilograms = Kilograms_Entry.get() 
     Kilograms = float(Kilograms)
     Grams = Kilograms * 1000
     Pounds = Kilograms * 2.20462
     Ounces = Kilograms * 35.274



     Alpha.config(text = f"Grams : {Grams:.2f} Grams")
     Bravo.config(text = f"Pounds : {Pounds:.2f}Pounds")
     Charlie.config(text = f"Ounces : {Ounces:.2f}Ounces")

Alpha = Label(tk, text = "")
Alpha.place(x = 85, y = 130)

Bravo = Label(tk, text = "")
Bravo.place(x = 85, y = 170)

Charlie = Label(tk, text = "")
Charlie.place(x = 85, y = 220)




Convert = Button(tk, text = "Convert", bg = "light blue", command = onclick).place(x = 115, y = 90)

tk.mainloop()