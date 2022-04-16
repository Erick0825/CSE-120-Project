import tkinter
from tkinter import *
from turtle import exitonclick
import vision_system
root = Tk()
class resultDisplay:
    def _init_(self):
        
        root.geometry("400x200")
        root['background'] = '#8a0602'
        root.title("Result")

    def display(self):
        if vision_system.match():
            label = tkinter.Label(text="Pass", background="#00FF00")
        else:
            label = tkinter.Label(text="Fail", background="#FF0000")
            
root.mainloop()