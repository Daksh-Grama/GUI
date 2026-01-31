from tkinter import*
from tkinter import ttk
from tkinter import messagebox
tk = Tk()
import random
tk.geometry("700x100")
tk.title("Rock Paper Scissors Shoot Game")
value = ["Rock", "Paper", "Scissors"]

d = Label(tk, text = "Choose Rock or Paper or Scissors and then press the enter button to submit your choice and then see if you win!")
d.place(x = 10, y = 10)



a = ttk.Combobox(tk, values = value)
a.place(x = 100, y = 41)
a.current(0)

ur_score = 0
comp_score =0 
e = Label(tk, text = f"Your score = {ur_score}")

f = Label(tk, text = f"Computer score = {comp_score}")

def EnTer():
    User = a.get()
    NuMber = random.choice(value)
    if User == NuMber:
        result = "Tie"
    elif ((User == "Rock" and NuMber == "Scissors") or (User == "Paper" and NuMber == "Rock") or (User == "Scissors" and NuMber == "Paper")):
        Result = "User wins!"
        ur_score += 1
    else:
        rEsult = "Computer wins"
        comp_score += 1
    e.config(text=f"Your Score: {ur_score}")
    f.config(text=f"Computer Score: {comp_score}")


    
    messagebox.showinfo("Who won", f" You chose {a.get()} and I chose {NuMber}")
    


 




b = Button(tk, text = "enter", command = EnTer)
b.place(x = 20, y = 40)



tk.mainloop()