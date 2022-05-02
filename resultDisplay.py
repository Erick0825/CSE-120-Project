import tkinter
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from setuptools import Command
# import vision_system


# command to go to camera page
def toCam():
    win.quit()

# command to go to start page
def toStart():
    win.destroy()
    import start_page
win = Tk()
# window created
def result():
    # window will display fail if vision_system passes "fail" result
    if bool(True):
        win.geometry("1000x900")
        # red
        win['background'] = '#FF0000'
        win.title("Result")
        msg = Label(win, text="Fail", font=('Sans', 72, BOLD),bg= '#FF0000')
        msg.place(relx=0.5, rely=0.4, anchor=CENTER)
        # camera page button
        camera = tk.Button(win, text="Camera", font=('Sans', 22, BOLD), padx=50, pady=20, command=toCam)
        camera.place(relx=0.3, rely=0.7, anchor=CENTER)
        # start page button
        start = tk.Button(win, text="Home", font=('Sans', 22, BOLD), padx=50, pady=20, command=toStart)
        start.place(relx=0.7, rely=0.7, anchor=CENTER)
    # window will display pass if vision_system passes "pass" result
    else:
        win.geometry("1000x900")
        # green
        win['background'] = '#00FF00'
        win.title("Result")
        msg = Label(win, text="Pass", font=('Sans', 72, BOLD), bg= '#00FF00')
        msg.place(relx=0.5, rely=0.4, anchor=CENTER)

        camera = tk.Button(win, text="Scan", font=('Sans', 22, BOLD), padx=50, pady=20, command=toCam)
        camera.place(relx=0.3, rely=0.7, anchor=CENTER)

        start = tk.Button(win, text="Home", font=('Sans', 22, BOLD), padx=50, pady=20, command=toStart)
        start.place(relx=0.7, rely=0.7, anchor=CENTER)

result()
win.mainloop()