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
    result = messagebox.askyesnocancel("Submit?","Sumbit final score?")
    if result == True: 
      messagebox.showinfo("Final","Score Saved")
      if result == False:
          messagebox.askokcancel("Score","Reset Score?")
      
    else:
         return
        
def show_message_and_save():
    response = messagebox.askyesno("Confirmation", "Are you sure?")
    if response:
        with open("saved_response.txt", "w") as file:
            file.write("Yes")
    else:
         with open("saved_response.txt", "w") as file:
            file.write("No")

class display():
   
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
    
    name_label = tk.Label(root,text = "1: ",bg="#044389")
    name_label.grid(row=1,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=1,column=1)

    name_label = tk.Label(root,text = "2: ", bg="#044389")
    name_label.grid(row=2,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=2,column=1)

    name_label = tk.Label(root,text = "3: ", bg="#044389")
    name_label.grid(row=3,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=3,column=1)

    name_label = tk.Label(root,text = "4: ", bg="#044389")
    name_label.grid(row=4,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=4,column=1)

    name_label = tk.Label(root,text = "5: ", bg="#044389")
    name_label.grid(row=5,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=5,column=1)

    name_label = tk.Label(root,text = "6: ", bg="#044389")
    name_label.grid(row=6,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=6,column=1)

    name_label = tk.Label(root,text = "Total score: ", bg="#044389")
    name_label.grid(row=7,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=7,column=1)

    name_label = tk.Label(root,text = "Bonus if 63 or more: ", bg="#044389")
    name_label.grid(row=8,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=8,column=1)

    name_label = tk.Label(root,text = "Total score for upper section: ", bg="#044389")
    name_label.grid(row=9,column = 0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=9,column=1)

    name_label = tk.Label(root,text = "3 of a kind: ", bg="#044389")
    name_label.grid(row=1,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=1,column=3)

    name_label = tk.Label(root,text = "4 of a kind: ", bg="#044389")
    name_label.grid(row=2,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=2,column=3)

    name_label = tk.Label(root,text = "Full House: ", bg="#044389")
    name_label.grid(row=3,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=3,column=3)

    name_label = tk.Label(root,text = "Small Straight: ", bg="#044389")
    name_label.grid(row=4,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=4,column=3)

    name_label = tk.Label(root,text = "Large Straight ", bg="#044389")
    name_label.grid(row=5,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=5,column=3)

    name_label = tk.Label(root,text = "Farkel: ", bg="#044389")
    name_label.grid(row=6,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=6,column=3)

    name_label = tk.Label(root,text = "Chance: ", bg="#044389")
    name_label.grid(row=7,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=7,column=3)

    name_label = tk.Label(root,text = "100 if got both bonuses: ", bg="#044389")
    name_label.grid(row=8,column = 2)
    name_entry = tk.Entry(root)
    name_entry.grid(row=8,column=3)

    name_label = tk.Label(root,text = "100 per other farkel: ", bg="#044389")
    name_label.grid(row=9,column =2 )
    name_entry = tk.Entry(root)
    name_entry.grid(row=9,column=3)


    label = Label(root, text="Please click the category you want to chart your score in:")
    label.grid(row=22,column=1,columnspan = 3)
                    
    button1 =tk. Button(root, text="ONES", bg="white", fg="black", width=20, font=("Times", 12))
    button1.grid(row=23, column=0)
                    
    button2 = tk.Button(root, text="TWOS", bg="white", fg="black", width=20, font=("Times", 12))
    button2.grid(row=23, column=1)
                    
    button3 = tk.Button(root, text="THREES", bg="white", fg="black", width=20, font=("Times", 12))
    button3.grid(row=23, column=2)
                    
    button4 = tk.Button(root, text="FOURS", bg="white", fg="black", width=20, font=("Times", 12))
    button4.grid(row=23, column=3)
                    
    button5 =tk. Button(root, text="FIVES", bg="white", fg="black", width=20, font=("Times", 12))
    button5.grid(row=23, column=4)
                    
    button6 = tk.Button(root, text="SIXES", bg="white", fg="black", width=20, font=("Times", 12))
    button6.grid(row=24, column=0)
                    
    button13 = tk.Button(root, text="YAHTZEE BONUS", bg="white", fg="black", width=20, font=("Times", 12))
    button13.grid(row=24, column=1)
                    
    button14 =tk.Button(root, text="CHANCE", bg="white", fg="black", width=20, font=("Times", 12),)
    button14.grid(row=24, column=2)

    button7 =tk. Button(root, text="THREE OF A KIND", bg="white", fg="black", width=20, font=("Times", 12))
    button7.grid(row=24, column=3)
                    
    button8 = tk.Button(root, text="FOUR OF A KIND", bg="white", fg="black", width=20, font=("Times", 12))
    button8.grid(row=24, column=4)
                    
    button9 = tk.Button(root, text="FULL HOUSE", bg="white", fg="black", width=20, font=("Times", 12))
    button9.grid(row=25, column=0)


    button10 =tk.Button(root, text="SMALL STRAIGHT", bg="white", fg="black", width=20, font=("Times", 12))
    button10.grid(row=25, column=1)

    button11 = tk.Button(root, text="LARGE STRAIGHT", bg="white", fg="black", width=20, font=("Times", 12))
    button11.grid(row=25, column=2)
                    
    button12 =tk.Button(root, text="YAHTZEE", bg="white", fg="black", width=20, font=("Times", 12))
    button12.grid(row=25, column=3)
    
    button25= tk.Button(root, text="History", bg="white", fg="black", width=20, font=("Times", 12))
    button25.grid(row=25, column=4)
    
    button26 = tk.Button(root, text="Options", bg="white", fg="black", width=20, font=("Times", 12))
    button26.grid(row=26, column=1,columnspan = 3) 
 

def dice_simulator():
        dicelist = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684'] 
      
      
        dice_one.config(text=f'{choice(dicelist)}')
        dice_two.config(text=f'{choice(dicelist)}')
        dice_three.config(text=f'{choice(dicelist)}')
        dice_four.config(text=f'{choice(dicelist)}')
        dice_five.config(text=f'{choice(dicelist)}')
        
heading_frame = Frame(root, bg="#044389")
heading_frame.grid(row=19,column=0)
        
dice_button_frame = Frame(root, bg="#044389", bd=2, relief=RAISED, pady=30, padx=20)
dice_button_frame.grid(row=19,column=0,columnspan=5)

dice_frame = Frame(dice_button_frame, bg="#044389")
dice_frame.grid(row=19,column=0)

button_frame = Frame(dice_button_frame, bg="#044389")
button_frame.grid(row=19,column=0)
        
dice_one = Label(dice_frame, text="\u2680", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_one.grid(row=20,column=0)

dice_two = Label(dice_frame, text="\u2681", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_two.grid(row=20,column=1)

dice_three = Label(dice_frame, text="\u2682", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_three.grid(row=20,column=2)

dice_four = Label(dice_frame, text="\u2683", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_four.grid(row=20,column=3)

dice_five = Label(dice_frame, text="\u2684", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_five.grid(row=20,column=4)

        
roll_dice_button = Button(button_frame, text="Roll Dice", font=("Times New Roman", "25"), bg="#044389", fg="#EEEEEE" ,command=dice_simulator)
roll_dice_button.grid(row=21,column=4,ipadx=30)

round_label = tk.Label(root,text =(f"  "), bg="#044389")
round_label.grid(row=28,column=1)
'''
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

def is_three_of_a_kind(dice):              #   
    for number in dice:                    # 
        if dice.count(number) >= 3:        # 
            return True                    # 
    return False  

def is_four_of_a_kind(dice):               #     
    for number in dice:                    # 
        if dice.count(number) >= 4:        # 
            return True                    # 
    return False  

def is_full_house(dice):                      #   
    diceset = set(dice)                       # 
    if len(diceset) == 2:                     # 
        for number in diceset:                # 
            if dice.count(number) in (2,3):   # 
                return True                   # 
    return False                              # 

def is_small_straight(dice):                  #  
    diceset = set(dice)                       # 
    if any((diceset.issuperset({1,2,3,4}),    # 
            diceset.issuperset({2,3,4,5}),
            diceset.issuperset({3,4,5,6}))):
        return True                           # 
    return False                          

def is_large_straight(dice):                  #  
    diceset = set(dice)                       # 
    if (diceset.issuperset({1,2,3,4,5}) or    # 
        diceset.issuperset({2,3,4,5,6})):
        return True                           # 
    return False   

def is_yahtzee(dice):                      #  
    return len(set(dice)) == 1             # 
    
def calculate_score(dice, name_of_option): #    
    assert len(dice) == 5, f"{dice} must have five elements" 
    error_message = f"{dice} must have only integers"
    assert [type(x) for x in dice] == [int,int,int,int,int], error_message 
    error_message = f"{name_of_option} must be in {all_options.keys()}"
    assert name_of_option in all_options, error_message 

    # joker rule?
    option_list = list(all_options) # 
    joker = False
    upper_name = option_list[dice[0]-1] # 
    if all((is_yahtzee(dice),           # 
            "Yahtzee" in history,
            upper_name in history)):
        joker = True
    match name_of_option:               # 
        # first test the lower section options
        case "Three Of A Kind":
            return sum(dice) if is_three_of_a_kind(dice) else 0 # 
        case "Four Of A Kind":
            return sum(dice) if is_four_of_a_kind(dice) else 0
        case  "Full House":
            return 25 if (is_full_house(dice) or joker) else 0
        case  "Small Straight":
            return 30 if (is_small_straight(dice) or joker) else 0
        case "Large Straight":
            return 40 if (is_large_straight(dice) or joker) else 0
        case "Yahtzee":
            return 50 if is_yahtzee(dice) else 0
        case "Chance":
            return sum(dice)
        case _:  
            # it's an upper section option:  Ones, Tows, ... Sixes
            number = option_list.index(name_of_option) + 1 # 
            return dice.count(number) * number             # 

def calculate_final_scores(history):   # 
    """returns a tuple of 4 integers: 
           sum_upper_section,
           upper_section_bonus,
           sum_lower_section,
           yahtzee_bonus
    """                                # 
    sum_upper_section = 0              # 
    sum_lower_section = 0
    upper_section_bonus = 0
    yahtzee_bonus = 0
    allow_yahtzee_bonus = False
    for name in history:               #      
        scored = history[name][0]      # 
        dice = history[name][1]        # 
        # is upper section?            # 
        if name in ("Ones", "Twos", "Threes",
                    "Fours", "Fives", "Sixes"):
            sum_upper_section += scored
        else:
            sum_lower_section += scored
        # is Yahtzee?                  # 
        if len(set(dice)) == 1: 
            # enable Yahtzee bonus ?
            if scored == 50 and not allow_yahtzee_bonus:
                allow_yahtzee_bonus = True
            elif allow_yahtzee_bonus:
                yahtzee_bonus += 100
    if sum_upper_section >= 63:        # 
        upper_section_bonus = 35
    return sum_upper_section, upper_section_bonus, sum_lower_section, yahtzee_bonus



def game():
    for game_round in range(1,14):                    
        dicelist = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684']                                      
        round_label = tk.Label(root,text =(f"------------round {game_round} of 13------------") , bg="#044389")
        for throw in (1,2,3):                         
            text= "throw: {} of 3".format(throw)      
            if throw < 3:
                #text = "Type letter(s) of dice to keep and press ENTER >>>"             
                for i, char in enumerate("abcde") :         
                    if char not in command:                
                        dicelist[i]    

        round_label = tk.Label(root,text =(f"------------round {game_round} of 13------------") , bg="#044389")
        # calculate playable options    # 
        unplayed = [name for name in all_options if name not in history]
        while True:                     #  
            # create menu, starting with number 1 for "Ones"
            for name in unplayed:     
                round_label = (list(all_options).index(name)+1, name) #  
            command = input("enter number of option to play >>>")
            try:                         # 
                number = int(command)    # 
            except ValueError:           # 
                print("Please enter only a NUMBER")
                continue                 # 
            if not (0 < number < 14):    # 
                round_label = ("Number out of allowed range, try again")
                continue                 # 
            option = list(all_options)[number-1] #  
            if option not in unplayed:   # 
                round_label =  (f"You already played {option}, try again")
                continue                 # 
            round_label = ("You play: ", option)
            break                        #  
        points = calculate_score(dicelist, option)
        round_label =  (f"you get {points} points!")
        if game_round == 13:                       
            text = "Press History to see the history of dice throws >>>"
        else:
            text = "Press Farkle to start the next game round >>>"
        input(text)                            
        history[option] = (points, dicelist.copy())  # 
    print("Game Over")  
    print("--- history of your dice throws: ---")
    print("game round,  played_option, points, dicelist")
    sum_upper, upper_bonus, sum_lower, yat_bonus = calculate_final_scores(history)
    print("option,          score (of max.)    dice")
    for name in all_options:
        print("{:<20}   {:>2} (of {:>2})   {:<20}".format(
            name,
            history[name][0],
            all_options[name],
            str(history[name][1])
        ))
        if name == "Sixes":
            print("-------------------------")
            print("sum upper section:", sum_upper)
            print("upper section bonus:", upper_bonus)
    print("--------------------")
    print("sum lower section", sum_lower)
    print("Yahtzee bonus:", yat_bonus)
    print("==========================")
    print("final score:",
           sum_upper+upper_bonus+sum_lower+yat_bonus)
    
            


if __name__ == "__main__":
    game()

    #,command=show_message_and_save   

''' 
    
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

 
button1= Button(window, text="Quit", bg="white", fg="black", width=20, font=("Times", 12),command=quit)
button2= Button(window, text="Rules", bg="white", fg="black", width=20, font=("Times", 12),command=rules)
button3= Button(window, text="Play A Game Of Farkle", bg="white", fg="black", width=20, font=("Times", 12),command = display)
 
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=1,column=6,padx=40,pady=10)


root.mainloop()


