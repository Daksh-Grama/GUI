from tkinter import*
root =Tk()
root.geometry("700x400")
root.config(background="red")
email = Label(root, text = "Email").place(x = 50, y = 70)
email_entry = Entry(root).place(x = 90, y = 70)

def onclick ():
    # print ("Entry Submitted!")

    Alpha.config(text = "Order Submitted!")

password = Label(root, text = "Password").place(x = 400, y = 70)
password_entry = Entry(root).place(x = 470, y = 70)


Food = Label(root, text = "What food would you like : Pav Bhaji, Puri Saagu, Veg Sandwich? or none").place(x = 90, y = 120)
Food_Entry = Entry(root, text = "Food").place(x = 50, y = 150)
Food_Spinbox = Spinbox(root, from_ = 0, to = 20, width = 20).place(x = 200, y = 150)


Beverage = Label(root, text = "What beverage would you like : Cola, Fanta, Apple Juice, Water? or none").place(x = 90, y = 200)
Beverage_Entry = Entry(root, text = "Beverage").place(x = 50, y = 230)
Beverage_Spinbox = Spinbox(root, from_ = 0, to = 20, width = 20).place(x = 200, y = 230)



Dessert = Label(root, text = "What dessert would you like : A Kulfi, a Brownie, a Milkshake? or none").place(x = 90, y = 280)
Dessert_Entry = Entry(root, text = "Dessert").place(x = 50, y = 310)
Dessert_Spinbox = Spinbox(root, from_ = 0, to = 20, width = 20).place(x = 200, y = 310)



Alpha = Label(root, text="")
Alpha.place(x = 450, y = 350)
Submit = Button(root, text = "Submit Order", bg = "white", command = onclick).place(x = 300, y = 350)




















































































































root.mainloop()