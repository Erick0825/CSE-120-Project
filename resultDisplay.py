import tkinter
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
# import vision_system

win = Tk()
# window created
def thisWindow():
    # window will display fail if vision_system passes "fail" result
    if bool(True):
        win.geometry("700x350")
        # red
        win['background'] = '#FF0000'
        win.title("Result")
        msg = Label(win, text="Fail", font=('Sans', 72, BOLD))
        msg.place(relx=0.5, rely=0.5, anchor=CENTER)
    # window will display pass if vision_system passes "pass" result
    else:
        win.geometry("700x350")
        # green
        win['background'] = '#00FF00'
        win.title("Result")
        msg = Label(win, text="Pass", font=('Sans', 72, BOLD))
        msg.place(relx=0.5, rely=0.5, anchor=CENTER)

thisWindow()
win.mainloop()