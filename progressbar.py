from TKinter import *
from tkinter.ttk import Progressbar

root = Tk()
root.geometry("670x677")
root.title("Progress Bar")
root.config(background = "blue")
PBar = Progressbar(root, orient = HORIZONTAL, length = 100, mode = "determinate")
PBar.place(x = 200, y = 400)

def Pbar():
    import time
    PBar["value"] = 12.5
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 25
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 37.5
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 50
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 62.5
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 75
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 87.5
    root.update_idletasks()
    time.sleep(2)

    PBar["value"] = 100
    root.update_idletasks()
    time.sleep(2)

Start = Button(root, text = "Start", bg = "light blue", command = Pbar).place(x = 150, y = 350)
root.mainloop()


