
from logging import root
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
# from turtle import position
# import Scan logo page.py
# to run in terminal go to CSE120 directory and call python3 bettsPage.py
"""key commands: 
setting background: bg=""
set foreground: fg = ""

"""
root = Tk()
def quit_window():
    root.destroy()

def initialWindow():
    # root = Tk()
    root.geometry("1920x1080")
    root['background'] = '#DFDDD1'
    root.title("Welcome Page")
# set the business logo on title 
    root.iconbitmap('out.jpg')
# def initClick(): <- how to create class to build functions for tkinter

    button1 = tk.Button(root, text="Detect With This Logo",font=('Sans',22,BOLD), padx= 20,pady=20)
# button1.grid(padx=10,pady=10)

    button1.place(relx= 0.58, rely = 0.8, anchor= NW)

    button2 = tk.Button(root, text="Use a different Logo", font=('Sans',22,BOLD), padx= 20,pady=20)
    button2.place(relx= 0.47, rely = 0.8, anchor= NE, )

root.mainloop()



