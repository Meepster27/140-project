import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import choice
from tkinter import Frame
from tkinter import Text
from tkinter import Label
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.messagebox import showinfo

window =tk.Tk()
window.title("Play game?")     
window.geometry("950x50+300+700")
window.configure(bg="BLACK")

root = tk.Tk()
root.title("Farkel")
root.geometry("950x1000+300+0")
root.configure(bg="#044389")
frame = Frame(root)
  
def action():
    result = messagebox.askyesnocancel("Submit?","Sumbit final score?" )
    if result == True: 
      image_path =("C:/Users/sharp/OneDrive/Pictures/140 class/congrats.png")
      messagebox.showinfo(image_path)
      if result == False:
          messagebox.askokcancel("Score","Reset Score?")
      else:
         return
def opt():
    result = messagebox.showinfo("Scores for:", "3 of a Kind =30 \n 4 of a kind= 30 \n FullHouse=25\n SS=30\n LS=40,\n Yahtzee =50 \n Chance =30")

def disable_entry(name_entry):
    name_entry1.config(state="disabled") 
    name_entry2.config(state="disabled")
    name_entry3.config(state="disabled")
    name_entry4.config(state="disabled")
    name_entry5.config(state="disabled")
    name_entry6.config(state="disabled")
    name_entry7.config(state="disabled")
    name_entry8.config(state="disabled")
    name_entry9.config(state="disabled")
    name_entry10.config(state="disabled")
    name_entry11.config(state="disabled")
    name_entry12.config(state="disabled")
    name_entry13.config(state="disabled")
    name_entry14.config(state="disabled")
    name_entry15.config(state="disabled")
    name_entry16.config(state="disabled")
    name_entry17.config(state="disabled")
    name_entry18.config(state="disabled")
    

def disable_button1():
    button1.config(state="disabled")
    
def disable_button2():
    button2.config(state="disabled")
    
def disable_button3():
    button3.config(state="disabled")
    
def disable_button4():
    button4.config(state="disabled")
    
def disable_button5():
    button5.config(state="disabled")
    
def disable_button6():
    button6.config(state="disabled")
    
def disable_button7():
    button7.config(state="disabled")
    
def disable_button8():
    button8.config(state="disabled")
    
def disable_button9():
    button9.config(state="disabled")
    
def disable_button10():
    button10.config(state="disabled")
    
def disable_button11():
    button11.config(state="disabled")
    
def disable_button12():
    button12.config(state="disabled")
    
def disable_button13():
    button13.config(state="disabled") 

def disable_button14():
    button14.config(state="disabled")             

all_options = {         
                                    # upper section:
        "Ones":            5,
        "Twos":            10,
        "Threes":          15,
        "Fours":           20,
        "Fives":           25,
        "Sixes":           30,
                                    # lower section
        "Three Of A Kind": 30,
        "Four Of A Kind":  30,
        "Full House":      25,
        "Small Straight":  30,
        "Large Straight":  40,
        "Yahtzee":         50,
        "Chance":          30,
        }
history = {}            



name_label1 = tk.Label(root,text = "1: ",bg="#044389")
name_label1.grid(row=1,column = 0)
name_entry1 = tk.Entry(root)
name_entry1.grid(row=1,column=1)
name_entry1.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label2 = tk.Label(root,text = "2: ", bg="#044389")
name_label2.grid(row=2,column = 0)
name_entry2 = tk.Entry(root)
name_entry2.grid(row=2,column=1)
name_entry2.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label3 = tk.Label(root,text = "3: ", bg="#044389")
name_label3.grid(row=3,column = 0)
name_entry3 = tk.Entry(root)
name_entry3.grid(row=3,column=1)
name_entry3.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label4 = tk.Label(root,text = "4: ", bg="#044389")
name_label4.grid(row=4,column = 0)
name_entry4 = tk.Entry(root)
name_entry4.grid(row=4,column=1)
name_entry4.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label5 = tk.Label(root,text = "5: ", bg="#044389")
name_label5.grid(row=5,column = 0)
name_entry5 = tk.Entry(root)
name_entry5.grid(row=5,column=1)
name_entry5.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label6 = tk.Label(root,text = "6: ", bg="#044389")
name_label6.grid(row=6,column = 0)
name_entry6 = tk.Entry(root)
name_entry6.grid(row=6,column=1)
name_entry6.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label7 = tk.Label(root,text = "Total score: ", bg="#044389")
name_label7.grid(row=7,column = 0)
name_entry7 = tk.Entry(root)
name_entry7.grid(row=7,column=1)
name_entry7.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label8 = tk.Label(root,text = "Bonus if 63 or more: ", bg="#044389")
name_label8.grid(row=8,column = 0)
name_entry8 = tk.Entry(root)
name_entry8.grid(row=8,column=1)
name_entry8.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label9 = tk.Label(root,text = "Total score for upper section: ", bg="#044389")
name_label9.grid(row=9,column = 0)
name_entry9 = tk.Entry(root)
name_entry9.grid(row=9,column=1)
name_entry9.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label10 = tk.Label(root,text = "3 of a kind: ", bg="#044389")
name_label10.grid(row=1,column = 2)
name_entry10 = tk.Entry(root)
name_entry10.grid(row=1,column=3)
name_entry10.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label11 = tk.Label(root,text = "4 of a kind: ", bg="#044389")
name_label11.grid(row=2,column = 2)
name_entry11 = tk.Entry(root)
name_entry11.grid(row=2,column=3)
name_entry11.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label12 = tk.Label(root,text = "Full House: ", bg="#044389")
name_label12.grid(row=3,column = 2)
name_entry12 = tk.Entry(root)
name_entry12.grid(row=3,column=3)
name_entry12.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label13 = tk.Label(root,text = "Small Straight: ", bg="#044389")
name_label13.grid(row=4,column = 2)
name_entry13 = tk.Entry(root)
name_entry13.grid(row=4,column=3)
name_entry13.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label14 = tk.Label(root,text = "Large Straight ", bg="#044389")
name_label14.grid(row=5,column = 2)
name_entry14 = tk.Entry(root)
name_entry14.grid(row=5,column=3)
name_entry14.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label15 = tk.Label(root,text = "Farkel: ", bg="#044389")
name_label15.grid(row=6,column = 2)
name_entry15 = tk.Entry(root)
name_entry15.grid(row=6,column=3)
name_entry15.bind("<Return>",disable_entry) # Disable on pressing Enter

name_label16 = tk.Label(root,text = "Chance: ", bg="#044389")
name_label16.grid(row=7,column = 2)
name_entry16 = tk.Entry(root)
name_entry16.grid(row=7,column=3)
name_entry16.bind("<Return>", disable_entry) # Disable on pressing Enter

name_label17 = tk.Label(root,text = "100 if got both bonuses: ", bg="#044389")
name_label17.grid(row=8,column = 2)
name_entry17 = tk.Entry(root)
name_entry17.grid(row=8,column=3)
name_entry17.bind("<Return>", disable_entry) # Disable on pressing Enter

name_label18 = tk.Label(root,text = "100 per other farkel: ", bg="#044389")
name_label18.grid(row=9,column =2 )
name_entry18 = tk.Entry(root)
name_entry18.grid(row=9,column=3)
name_entry18.bind("<Return>",disable_entry) # Disable on pressing Enter

label20 = Label(root, text="Please click the category you want to chart your score in:")
label20.grid(row=15,column=1,columnspan = 3)

button1 =tk.Button(root, text="ONES", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button1)
button1.grid(row=16, column=0)


button2 = tk.Button(root, text="TWOS", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button2)
button2.grid(row=16, column=1)

button3 = tk.Button(root, text="THREES", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button3)
button3.grid(row=16, column=2)

button4 = tk.Button(root, text="FOURS", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button4)
button4.grid(row=16, column=3)

button5 =tk.Button(root, text="FIVES", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button5)
button5.grid(row=16, column=4)

button6 = tk.Button(root, text="SIXES", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button6)
button6.grid(row=17, column=0)

button7 =tk.Button(root, text="THREE OF A KIND", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button7)
button7.grid(row=17, column=1)

button8 = tk.Button(root, text="FOUR OF A KIND", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button8)
button8.grid(row=17, column=2)

button9 = tk.Button(root, text="FULL HOUSE", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button9)
button9.grid(row=17, column=3)

button10 =tk.Button(root, text="SMALL STRAIGHT", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button10)
button10.grid(row=17, column=4)

button11 = tk.Button(root, text="LARGE STRAIGHT", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button11)
button11.grid(row=18, column=0)
                
button12 =tk.Button(root, text="YAHTZEE", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button12)
button12.grid(row=18, column=1)

button13 = tk.Button(root, text="YAHTZEE BONUS", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button13)
button13.grid(row=18, column=2)
             
button14 =tk.Button(root, text="CHANCE", bg="white", fg="black", width=20, font=("Times", 12),state="normal",command =disable_button14)
button14.grid(row=18, column=3)

button15= tk.Button(root, text="History", bg="white", fg="black", width=20, font=("Times", 12))
button15.grid(row=18, column=4)

button16 = tk.Button(root, text="Options", bg="white", fg="black", width=20, font=("Times", 12),command=opt)
button16.grid(row=19, column=1,columnspan=3)





def dice_simulator():
        
        dicelist = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684'] 
      
        dice_one.config(text=f'{choice(dicelist)}')
        dice_two.config(text=f'{choice(dicelist)}')
        dice_three.config(text=f'{choice(dicelist)}')
        dice_four.config(text=f'{choice(dicelist)}')
        dice_five.config(text=f'{choice(dicelist)}')
        
heading_frame = Frame(root, bg="#044389")
heading_frame.grid(row=10,column=0)

dice_button_frame = Frame(root, bg="#044389", bd=2, relief=RAISED, pady=30, padx=20)
dice_button_frame.grid(row=12,column=0,columnspan=5) 

dice_frame = Frame(dice_button_frame, bg="#044389")
dice_frame.grid(row=10,column=0)

button_frame = Frame(dice_button_frame, bg="#044389")
button_frame.grid(row=11,column=0)

var1 = tk.IntVar()
def disable_dice1():
    if var1.get():
     dice_one.config(state="normal")
    else: 
      dice_one.config(state="disabled")

checkbox1 = tk.Checkbutton(root, text='Lock 1',font="Courier 25", bg="#044389", variable=var1, command= disable_dice1).grid(row=14,column=0 ,sticky=W)
dice_one = Label(dice_frame, text="\u2680", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_one.grid(row=11,column=0)

var2 = IntVar()
def disable_dice2():
    if var2.get():
     dice_two.config(state="normal")
    else: dice_two.config(state="disabled")
dice_two = Label(dice_frame, text="\u2681", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_two.grid(row=11,column=1)
Checkbutton(root, text='Lock 2',font="Courier 25", bg="#044389", variable=var2,command= disable_dice2).grid(row=14,column=1, sticky=W)

var3 = IntVar()
def disable_dice3():
    if var3.get():
     dice_three.config(state="normal")
    else: dice_three.config(state="disabled")
dice_three = Label(dice_frame, text="\u2682", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_three.grid(row=11,column=2)
Checkbutton(root, text='Lock 3',font="Courier 25", bg="#044389", variable=var3,command= disable_dice3).grid(row=14,column=2, sticky=W)

var4 = IntVar()
def disable_dice4():
    if var4.get():
     dice_four.config(state="normal")
    else: dice_four.config(state="disabled")
dice_four = Label(dice_frame, text="\u2683", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_four.grid(row=11,column=3)
Checkbutton(root, text='Lock 4',font="Courier 25", bg="#044389", variable=var4,command= disable_dice4).grid(row=14,column=3, sticky=W)

var5 = IntVar()
def disable_dice5():
    if var5.get():
     dice_five.config(state="normal")
    else: dice_five.config(state="disabled")
dice_five = Label(dice_frame, text="\u2684", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_five.grid(row=11,column=4)
Checkbutton(root, text='Lock 5',font="Courier 25", bg="#044389", variable=var5,command= disable_dice5).grid(row=14,column=4 ,sticky=W)


      
roll_dice_button = Button(button_frame, text="Roll Dice", font=("Times New Roman", "25"), bg="#044389", fg="#EEEEEE" ,command=dice_simulator)
roll_dice_button.grid(row=13,column=1,ipadx=30)

round_label = tk.Label(root,text =(f"  "), bg="#044389")
round_label.grid(row=22,column=1)

class display():
    import random
    history = {}
    all_options = {         
                                       # upper section:
           "Ones":            5,
           "Twos":            10,
           "Threes":          15,
           "Fours":           20,
           "Fives":           25,
           "Sixes":           30,
                                        # lower section
           "Three Of A Kind": 30,
           "Four Of A Kind":  30,
           "Full House":      25,
           "Small Straight":  30,
           "Large Straight":  40,
           "Yahtzee":         50,
           "Chance":          30,
           }
    

def quit():
    exit()
 
def rules():
    showinfo('RULES','The game begins by the player rolling a cup of five dice. The player may roll the 5 dice a total'
          ' of 3 times. After each roll the player may set aside any dice they wish to keep for scoring and place the others'
          ' back in the cup. Then the player must choose a category to score the points. Scoring can be charted at any'
          ' point in the round. The player does not have to roll the dice three times.'
    '\n\nSCORING\n'
 
    '\nTo chart your score choose one of the categories on the scorecard. Once you place a score in a category \n'
          'it cannot be scored again the rest of the game, except for the "Yahtzee" Bonus. The player with the most \n'
          'points after all categories have been filled wins the game. Listed below is an explanation of the scoring for each category:\n\n'
          'UPPER SECTION SCORING\n\n'
          'ONES: The sum of all the 1s rolled by the player.\n'
          'TWOS: The sum of all the 2s rolled by the player.\n'
          'THREES: The sum of all the 3s rolled by the player.\n'
          'FOURS: The sum of all the 4s rolled by the player.\n'
          'FIVES: The sum of all the 5s rolled by the player.\n'
          'SIXES: The sum of the 6s rolled by the player.\n'
          'TOTAL SCORE: The sum of the 6 categories above.\n'
          'BONUS: If the total score is 63 or greater a bonus score of 35 is added.\n'
          'TOTAL UPPER SECTION: The total score plus the bonus if one is given.\n\n'
 
          'LOWER SECTION SCORING\n\n'
 
          'THREE OF A KIND: Scores the total of all dice and must include 3 of the same number.\n'
          'FOUR OF A KIND: Scores the total of all dice and must include 4 of the same number.\n'
          'FULL HOUSE: Scored as 25 points and must include 3 dice of one number and 2 dice of another number.\n'
          'SMALL STRAIGHT: Scored as 30 points and is a sequence of 4 numbers.\n'
          'LARGE STRAIGHT: Scored as 40 points and is a sequence of 5 numbers.\n'
          'YAHTZEE: Scored as 50 points and is a 5 of a kind.(5 dice of the same number)\n'
          'CHANCE: Total of all 5 dice.\n'
          '"YAHTZEE BONUS": Scored as 100 points and this category is charted for each additonal "Yahtzee" rolled.\n'
          'LOWER SECTION TOTAL: Sum of all categories in the lower section.\n'
 
          '\nGRAND TOTAL: The sum of the upper section total and the lower section total.\n')

 
button20= Button(window, text="Quit", bg="white", fg="black", width=20, font=("Times", 12),state = 'normal',command=quit)
button21= Button(window, text="Rules", bg="white", fg="black", width=20, font=("Times", 12),state = 'normal',command=rules)
button22= Button(window, text="Submit Score?", bg="white", fg="black", width=20, font=("Times", 12),state= 'normal',command=action) 
 
button20.grid(row=1,column=4, padx=40, pady=10)
button21.grid(row=1,column=5, padx=40, pady=10)
button22.grid(row=1,column=6,padx=40,pady=10)


root.mainloop()
