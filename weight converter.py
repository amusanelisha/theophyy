from tkinter import *
root = Tk()
label_1 = Label(root, text = 'Enter the weight in Kg')
label_1.grid(row = 0, column = 0)

label_2 = Label(root, text = 'GRAM' )
label_2.grid(row = 2, column =1)

label_3 = Label(root, text = 'POUNDS')
label_3.grid(row = 2 , column = 2, padx = 10, pady = 10)

label_4 = Label(root, text = 'OUNCE')
label_4.grid(row = 2 , column = 3, padx = 10, pady =10)

#entry box
entry_1 = Entry(root, width = 30)
entry_1.grid(row = 0, column = 1)
entry_2 = Entry(root, width = 30)
entry_2.grid(row = 3, column = 1)
entry_3 = Entry(root, width = 30)
entry_3.grid(row = 3, column = 2)
entry_4 = Entry(root, width = 30)
entry_4.grid(row = 3, column = 3)

def conversion():
    conv = float(entry_1.get())
    conv_1 = conv * 1000
    conv_2 = conv * 2.20462
    conv_3 = conv* 35.274
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_2.insert(0, conv_1)
    entry_3.insert(0, conv_2)
    entry_4.insert(0, conv_3)
    
def Reset(): 
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)

#button widget
button_1 = Button(root, text = "Convert", command = conversion)
button_1.grid(row = 1 , column = 2)
button_2 = Button(root, text = "Reset", command = Reset)
button_2.grid(row = 1 , column = 4)

mainloop()