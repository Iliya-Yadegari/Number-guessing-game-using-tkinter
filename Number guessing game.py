from tkinter import *
import random
import math

def main_fun():

    global lower
    lower = int(lower_ent.get())

    global upper
    upper = int(upper_ent.get())

    global horizontal
    horizontal = Scale(window,from_ = lower,to = upper,orient = HORIZONTAL)


    guessNum_lbl = Label(window,text = "\n\tYou've only "+str(round(math.log(upper - lower + 1, 2)))+" chances to guess the integer!\n").grid(row = 4, column = 0, padx = 10, pady = 10)

    horizontal.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    sub_btn = Button(window,text = 'Submit',height = 3,width = 20,command = res_fun)

    sub_btn.grid(row = 6, column = 0, padx = 10, pady = 10)



def res_fun():
    
    x = random.randint(lower, upper)
    
    count = 0
    
    while count < math.log(upper - lower + 1, 2):
        count += 1
     

        if x == horizontal.get():
            txt = "Congratulations you did it in ",count, " try"

            break
        elif x > horizontal.get():
            txt = "You guessed too small!"
        elif x < horizontal.get():
            txt = "You Guessed too high!"

        if count >= math.log(upper - lower + 1, 2):
            txt = "\nThe number is %d" % x,"\tBetter Luck Next time!"
        
        messagebox.showinfo('Result',txt)


window = Tk()
window.title('Number guessing game')

main_frm = LabelFrame(window).grid(row = 0, column = 0, padx = 10, pady = 10)

lower_lbl = Label(main_frm,text = 'Enter your lower bound ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
lower_ent = Entry(main_frm)
upper_lbl = Label(main_frm,text = 'Enter your upper bound ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
upper_ent = Entry(main_frm)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = main_fun).grid(row = 2, column = 0, padx = 10, pady = 10)

lower_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
upper_ent.grid(row = 1, column = 1, padx = 10, pady = 10)

window.mainloop()