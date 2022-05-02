from logging import root
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from setuptools import Command


# to run in terminal go to CSE120 directory and call python3 bettsPage.py

# this function closes the window, if added in button with command= it will close window after closing
def quitpage():
    root.quit()

def go_to_next():
    root.destroy()
    import Scan_logo_page
root = Tk()


def startwindow():   
    root.geometry("1000x900")
    root['background'] = '#DFDDD1'
    
    root.title("Welcome")

    # def initClick(): <- how to create class to build functions for tkinter
    msg = Label(root, text="Hello, Welcome to Bett's Logo Detector!", font=('Sans', 26, BOLD),fg='black')
    msg.config(bg= '#DFDDD1')
    msg.place(relx=0.5, rely=0.2, anchor=CENTER)

    start = tk.Button(root, text="Start", font=('Sans', 26, BOLD), padx=50, pady=20, command=go_to_next)

    start.place(relx=0.5, rely=0.7, anchor=CENTER)

img=PhotoImage(file='betts.png')
img_place = Label(root,image=img,)
img_place.config(bg= '#DFDDD1')
img_place.place(relx=0.5, rely=0.9, anchor=CENTER)


startwindow()
root.mainloop()
