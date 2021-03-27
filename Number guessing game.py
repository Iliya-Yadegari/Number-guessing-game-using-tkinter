from tkinter import *





window = Tk()
window.title('Number guessing game')

main_frm = LabelFrame(window).grid(row = 0, column = 0, padx = 10, pady = 10)

lower_lbl = Label(main_frm,text = 'Enter your lower bound ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
lower_ent = Entry(main_frm).grid(row = 0, column = 1, padx = 10, pady = 10)
upper_lbl = Label(main_frm,text = 'Enter your upper bound ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
upper_ent = Entry(main_frm).grid(row = 1, column = 1, padx = 10, pady = 10)

window.mainloop()