import tkinter as tk
from tkinter import Entry, messagebox
from tkinter import*
d = tk.Tk()
d.geometry("300x300")
d.title("Countdown")

Hours = Entry(d, width = 5)
Hours.place(x = 1, y =50)
Hours.insert(0, "0")

Minutes = Entry(d, width = 5)
Minutes.place(x = 125, y =50)
Minutes.insert(0, "0")

Seconds = Entry(d, width = 5)
Seconds.place(x = 250, y =50)
Seconds.insert(0, "0")



def Start_Timer():
    Hour = Hours.get()
    Minute = Minutes.get()
    Second = Seconds.get()

    if Hour.isdigit() and Minute.isdigit() and Second.isdigit():
        Hour = int(Hour)
        Minute = int(Minute)
        Second = int(Second)

    if Second>=60:
        Minute += Second//60
        Second = Second % 60

        Minute.delete(0, tk.END)
        Minute.insert(0, Minute)

        Second.delete(0, tk.END)
        Second.insert(0, Second)
    Total_Second = Hour*3600 + Minute*60 + Second
    countdown(Total_Second)

def countdown(Total_Second):
    if Total_Second > 0:
        hours = Total_Second//3600
        minutes = (Total_Second % 3600)//60
        seconds = Total_Second % 60

        Hours.delete(0, tk.END)
        Hours.insert(0, hours)

        Minutes.delete(0, tk.END)
        Minutes.insert(0, minutes)

        Seconds.delete(0, tk.END)
        Seconds.insert(0, seconds)
        d.after(1000, countdown, Total_Second - 1)

    else:
        messagebox.showinfo("TIMES UP !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    



submit = Button(d, text = "Submit", bg = "light blue", command = Start_Timer)
submit.place(x = 125, y = 150)

tk.mainloop()
