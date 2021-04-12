from tkinter import *
import random
import math
import NumberGuessingGame as ngg

def main_fun():

    lower = int(ngg.lower_ent.get())

    upper = int(ngg.upper_ent.get())    

    global x
    x = random.randint(lower, upper)



    global horizontal
    horizontal = Scale(window,from_ = lower,to = upper,orient = HORIZONTAL)


    guessNum_lbl = Label(window,text = "\n\tYou've only "+str(round(math.log(upper - lower + 1, 2)))+" chances to guess the integer!\n").grid(row = 4, column = 0, padx = 10, pady = 10)

    horizontal.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    sub_btn = Button(window,text = 'Submit',height = 3,width = 20,command = res_fun)

    sub_btn.grid(row = 6, column = 0, padx = 10, pady = 10)



def res_fun():

    global count
    count += 1
    
    # count = 0
    
    # while count < math.log(upper - lower + 1, 2):
    #     count += 1
     
    lower = int(lower_ent.get())
    upper = int(upper_ent.get())

    if x == horizontal.get():
        txt = "Congratulations you did it in ",count, " try"

            
    elif x > horizontal.get():
        txt = "You guessed too small!"
    elif x < horizontal.get():
        txt = "You Guessed too high!"

    if count >= math.log(upper - lower + 1, 2):
        txt = "\nThe number is %d" % x,"\tBetter Luck Next time!"
        
    messagebox.showinfo('Result',txt)