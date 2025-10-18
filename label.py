from tkinter import*
root =Tk()
root.geometry("500x500")
root.config(background="light blue")
username = Label(root, text="Username").place(x = 50, y = 70)

username_entry = Entry(root).place(x = 150, y = 70)

password = Label(root, text="Password").place(x = 50, y = 120)

password_entry = Entry(root).place(x = 150, y = 120)

def onclick ():
    # print ("Entry Submitted!")

    Alpha.config(text = "Entry Submitted!")

Alpha = Label(root, text="")
Alpha.place(x = 150, y = 170)
Submit = Button(root, text = "Submit", bg = "light blue", command = onclick).place(x = 50, y = 170)


spin = Spinbox(root, from_=0, to=100000, width = 50).place(x = 150, y = 220)


root.mainloop()