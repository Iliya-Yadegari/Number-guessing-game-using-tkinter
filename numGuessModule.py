from tkinter import *
import random
import math

count = 0

def main_fun(lower_e,upper_e,w):
    global lower
    lower = int(lower_e)

    global upper
    upper = int(upper_e)    

    global x
    x = random.randint(lower, upper)

    global horizontal
    horizontal = Scale(w,from_ = lower,to = upper,orient = HORIZONTAL)

    guessNum_lbl = Label(w,text = "\n\tYou've only "+str(round(math.log(upper - lower + 1, 2)))+" chances to guess the integer!\n").grid(row = 4, column = 0, padx = 10, pady = 10)

    horizontal.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    sub_btn = Button(w,text = 'Submit',height = 3,width = 20,command = res_fun)

    sub_btn.grid(row = 6, column = 0, padx = 10, pady = 10)

def res_fun():

    global count
    count += 1
        
    # while count < math.log(upper - lower + 1, 2):
    #     count += 1
     
    if x == horizontal.get():
        txt = "Congratulations you did it in ",count, " try"
            
    elif x > horizontal.get():
        txt = "You guessed too small!"
    elif x < horizontal.get():
        txt = "You Guessed too high!"

    if count >= math.log(upper - lower + 1, 2):
        txt = "\nThe number is %d" % x,"\tBetter Luck Next time!"
        
    messagebox.showinfo('Result',txt)