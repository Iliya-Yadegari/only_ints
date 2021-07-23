from tkinter import *

def only_ints():
    try:
        int_1 = int(num1_ent.get())
        int_2 = int(num2_ent.get())

        res_label = Label(window,text = 'True')
        
    except:
        res_label = Label(window,text = 'False')
    
    res_label.grid(row = 3, column = 0, padx = 10, pady = 10)

window = Tk()

window.title('only_ints')

num1_lbl = Label(window,text = 'Enter your first number: ').grid(row = 0, column = 0, padx = 10, pady = 10)
num1_ent = Entry(window)
num2_lbl = Label(window,text = 'Enter your second number: ').grid(row = 1, column = 0, padx = 10, pady = 10)
num2_ent = Entry(window)
submit_btn = Button(window,text = 'Submit',command = only_ints,width = 20,height = 3).grid(row = 2, column = 0, padx = 10, pady = 10)

num1_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
num2_ent.grid(row = 1, column = 1, padx = 10, pady = 10)

window.mainloop()