from tkinter import *
import random
import math

def main_fun():

    lower = lower_ent.get()

    upper = upper_ent.get()

    horizontal = Scale(window,from_ = lower,to = upper,orient = HORIZONTAL)

    x = random.randint(lower, upper)
    guessNum_lbl = Label(window,text = "\n\tYou've only "+round(math.log(upper - lower + 1, 2))+" chances to guess the integer!\n").grid(row = 4, column = 0, padx = 10, pady = 10)

    horizontal.grid(row = 5, column = 0, padx = 10, pady = 10)

    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
     
        guess_ent = Entry()

        if x == guess:
            txt = "Congratulations you did it in ",count, " try"

            break
        elif x > guess:
            txt = "You guessed too small!"
        elif x < guess:
            txt = "You Guessed too high!"

        if count >= math.log(upper - lower + 1, 2):
            txt = "\nThe number is %d" % x,"\tBetter Luck Next time!"
        
        messagebox.showinfo('Result',txt)
window = Tk()
window.title('Number guessing game')

main_frm = LabelFrame(window).grid(row = 0, column = 0, padx = 10, pady = 10)

lower_lbl = Label(main_frm,text = 'Enter your lower bound ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
lower_ent = Entry(main_frm).grid(row = 0, column = 1, padx = 10, pady = 10)
upper_lbl = Label(main_frm,text = 'Enter your upper bound ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
upper_ent = Entry(main_frm).grid(row = 1, column = 1, padx = 10, pady = 10)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = main_fun).grid(row = 2, column = 0, padx = 10, pady = 10)

window.mainloop()