import tkinter
from tkinter import *


master = Tk()
master.geometry("400x200")
master['background'] = '#8a0602'
# style = ttk.Style(master)


master.title("Welcome!")


button1 = tkinter.Button(master, text="Detect With This Logo", highlightbackground='#3E4149')
button1.grid(row=1, column=0)
button1.pack(side='bottom')

button2 = tkinter.Button(master, text="Use a different Logo")
button2.grid(row=1, column=2)
button2.pack(side='bottom')
master.mainloop(0)

