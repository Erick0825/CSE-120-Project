from logging import root
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
from tkinter.font import BOLD
import tkinter as tk
from setuptools import Command
#below is for image display (not sure if it works)
#from PIL import ImageTk, Image
import Scan_logo_page
import resultDisplay

def confirmpage(vision):
    root = Tk()
    root.title("Confirmation Page")
    root.geometry("1920x1080")
    root['background'] = '#DFDDD1'

    #also for image display(not sure if it works)
    #path = uploadFiles()
    #img = ImageTk.PhotoImage(Image.open(path))
    #panel = tk.Label(window, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")


    # change imports in the two def to adjust
    def previouspage():
        root.destroy()
        Scan_logo_page.scanlogopage(vision)

    def nextpage():
        root.destroy()
        resultDisplay.resultdisplay(vision)

    msg = Label(root, text="Is This The Image You Want To Use?", font=('Sans', 26, BOLD))
    msg.place(relx=0.5, rely=0.1, anchor=CENTER)

    start = tk.Button(root, text="Yes, continue", font=('Sans', 22, BOLD), padx=30, pady=20, command=nextpage)
    start.place(relx=0.3, rely=0.7, anchor=CENTER)

    start = tk.Button(root, text="No, select again", font=('Sans', 22, BOLD), padx=30, pady=20, command=previouspage)
    start.place(relx=0.7, rely=0.7, anchor=CENTER)

    root.mainloop()