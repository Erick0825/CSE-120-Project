
from logging import root
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD

from setuptools import Command
# from turtle import position
# import Scan logo page.py
# to run in terminal go to CSE120 directory and call python3 bettsPage.py

# this function closes the window, if added in button with command= it will close window after closing
def quitPage():
    root.quit()
root= Tk()    
def startWindow():
    
    root.geometry("1920x1080")
    root['background'] = '#DFDDD1'
    root.title("Welcome Page")
# set the business logo on title 
    root.iconbitmap('out.jpg')
# def initClick(): <- how to create class to build functions for tkinter
    msg = Label(root, text = "Hello, Welcome to Bett's Logo Detector",font=('Sans',26,BOLD))
    msg.place(relx= 0.5, rely = 0.2, anchor= CENTER )
    
    start = tk.Button(root, text="Start",font=('Sans',22,BOLD), padx= 50,pady=20,command= quitPage)

    start.place(relx= 0.5, rely = 0.7, anchor= CENTER)
"""
    button2 = tk.Button(root, text="Use a different Logo", font=('Sans',22,BOLD), padx= 20,pady=20)
    button2.place(relx= 0.47, rely = 0.8, anchor= NE )"""


startWindow()
root.mainloop()


