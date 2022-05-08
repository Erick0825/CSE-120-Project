import tkinter
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from setuptools import Command
# import vision_system
import start_page
import Scan_logo_page

def resultdisplay(vision):
    win = Tk()
    # command to go to camera page
    def toCam():
        win.destroy()
        Scan_logo_page.scanlogopage(vision)

    # command to go to start page
    def toStart():
        win.destroy()
        start_page.startpage(vision)

    # window created
    def result(detection_result):
        # window will display fail if vision_system passes "fail" result
        if detection_result:
            win.geometry("1000x900")
            # red
            win['background'] = '#FF0000'
            win.title("Result")
            msg = Label(win, text="Fail", font=('Sans', 72, BOLD),bg= '#FF0000')
            msg.place(relx=0.5, rely=0.4, anchor=CENTER)
            # camera page button
            camera = tk.Button(win, text="Scan Another Image", font=('Sans', 22, BOLD), padx=50, pady=20, command=toCam)
            camera.place(relx=0.3, rely=0.7, anchor=CENTER)
            # start page button
            start = tk.Button(win, text="Home", font=('Sans', 22, BOLD), padx=50, pady=20, command=toStart)
            start.place(relx=0.7, rely=0.7, anchor=CENTER)
        # window will display pass if vision_system passes "pass" result
        else:
            win.geometry("700x350")
            # green
            win['background'] = '#00FF00'
            win.title("Result")
            msg = Label(win, text="Pass", font=('Sans', 72, BOLD),bg='#00FF00')
            msg.place(relx=0.5, rely=0.4, anchor=CENTER)

            camera = tk.Button(win, text="Scan Another Image", font=('Sans', 22, BOLD), padx=50, pady=20, command=toCam)
            camera.place(relx=0.3, rely=0.7, anchor=CENTER)

            start = tk.Button(win, text="Home", font=('Sans', 22, BOLD), padx=50, pady=20, command=toStart)
            start.place(relx=0.7, rely=0.7, anchor=CENTER)

    result(not (vision.threshold <= vision.match()))
    win.mainloop()