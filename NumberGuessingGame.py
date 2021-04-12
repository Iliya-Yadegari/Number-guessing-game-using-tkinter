from tkinter import *
import random
import math

import numGuessModule as ngm


window = Tk()
window.title('Number guessing game')

main_frm = LabelFrame(window).grid(row = 0, column = 0, padx = 10, pady = 10)

count = 0

lower_lbl = Label(main_frm,text = 'Enter your lower bound ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
lower_ent = Entry(main_frm)
upper_lbl = Label(main_frm,text = 'Enter your upper bound ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
upper_ent = Entry(main_frm)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = ngm.main_fun).grid(row = 2, column = 0, padx = 10, pady = 10)

lower_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
upper_ent.grid(row = 1, column = 1, padx = 10, pady = 10)

window.mainloop()