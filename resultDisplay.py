import tkinter
from tkinter import *
from turtle import exitonclick
from vision_system import vision_system

root = Tk()


def display():
    if vision_system.match():
        label = tkinter.Label(text="Pass", background="#00FF00")
    else:
        label = tkinter.Label(text="Fail", background="#FF0000")


def _init_():
    
    root.geometry("400x200")
    root['background'] = '#8a0602'
    root.title("Result")


class resultDisplay:
    pass


root.mainloop()
