from tkinter import*
from tkinter import messagebox
import random

tk = Tk()
tk.geometry("300x300")
tk.title("Guess The Number Game")
Enter_Your_Name = Label(tk, text = "Enter your name : ")
Enter_Your_Name.place(x = 10, y = 10)
Name_entry = Entry(tk)
Name_entry.place(x = 110, y = 10)

def onclick ():
    messagebox.showinfo("Information", f"Hello {Name_entry.get()}! Welcome to the Guess The Number Game! In this game you have to guess a number between 1 and 20 !")
Number = random.randint(1, 20)


def Guess ():
    User_Guess = int(Guess_entry.get())
    if User_Guess > 20:
        messagebox.showinfo("ERROR", "ERROR NUMBER IS HIGHER THAN 20!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif User_Guess > Number:
        messagebox.showinfo("Information", "Your guess is too high!")
   
    elif User_Guess < Number:
        messagebox.showinfo("Information", "Your guess is too low!")
    else:           
        messagebox.showinfo("Information", "Congratulations! You guessed it right!")

    




Enter_Your_Guess = Label(tk, text = "Enter your Guess : ")
Enter_Your_Guess.place(x = 10, y = 90)
Guess_entry = Entry(tk)
Guess_entry.place(x = 110, y = 90)













guess = Button(tk, text = "Ok", bg = "light blue", command = Guess)
guess.place(x = 250, y = 90)








Ok = Button(tk, text = "Ok", bg = "light blue", command = onclick)
Ok.place(x = 250, y = 10)
















































tk.mainloop()