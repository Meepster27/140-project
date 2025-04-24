import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
 
import random

def action():
    result = messagebox.askyesnocancel("Submit?","Sumbit final score?")
    if result == True: 
      messagebox.showinfo("Final","Score Saved")
      if result == False:
          messagebox.askokcancel("Score","Reset Score?")
      
    else:
         return
root = tk.Tk()
root.title("Farkle")
root.geometry("800x300")#W * L




name_label = tk.Label(root,text = "1: ")
name_label.grid(row=1,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=1,column=1)

name_label = tk.Label(root,text = "2: ")
name_label.grid(row=2,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=2,column=1)

name_label = tk.Label(root,text = "3: ")
name_label.grid(row=3,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=3,column=1)

name_label = tk.Label(root,text = "4: ")
name_label.grid(row=4,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=4,column=1)

name_label = tk.Label(root,text = "5: ")
name_label.grid(row=5,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=5,column=1)

name_label = tk.Label(root,text = "6: ")
name_label.grid(row=6,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=6,column=1)

name_label = tk.Label(root,text = "Total score: ")
name_label.grid(row=7,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=7,column=1)

name_label = tk.Label(root,text = "Bonus if 63 or more: ")
name_label.grid(row=8,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=8,column=1)

name_label = tk.Label(root,text = "Total score for upper section: ")
name_label.grid(row=9,column = 0)
name_entry = tk.Entry(root)
name_entry.grid(row=9,column=1)

name_label = tk.Label(root,text = "3 of a kind: ")
name_label.grid(row=1,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=1,column=3)

name_label = tk.Label(root,text = "4 of a kind: ")
name_label.grid(row=2,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=2,column=3)

name_label = tk.Label(root,text = "Full House: ")
name_label.grid(row=3,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=3,column=3)

name_label = tk.Label(root,text = "Small Straight: ")
name_label.grid(row=4,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=4,column=3)

name_label = tk.Label(root,text = "Large Straight ")
name_label.grid(row=5,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=5,column=3)

name_label = tk.Label(root,text = "Farkel: ")
name_label.grid(row=6,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=6,column=3)

name_label = tk.Label(root,text = "Chance: ")
name_label.grid(row=7,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=7,column=3)

name_label = tk.Label(root,text = "100 if got both bonuses: ")
name_label.grid(row=8,column = 2)
name_entry = tk.Entry(root)
name_entry.grid(row=8,column=3)

name_label = tk.Label(root,text = "100 per other farkel: ")
name_label.grid(row=9,column =2 )
name_entry = tk.Entry(root)
name_entry.grid(row=9,column=3,)


option1=tk.Button(root,text = "Submit score", command = action)
option1.grid(row=12,column=1 ,sticky = "ew",columnspan = 6, padx = 20 )


root.mainloop()
