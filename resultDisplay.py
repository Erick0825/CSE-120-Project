import tkinter
from tkinter import *
from turtle import exitonclick
from vision_system import vision_system

class resultDisplay:
    def _init_(self):
        main.geometry("400x200")
        main['background'] = '#8a0602'
        main.title("Result")

    def display(self):
        if vision_system.match():
            label = tkinter.Label(text="Pass", background="#00FF00")
        else:
            label = tkinter.Label(text="Fail", background="#FF0000")

main = Tk()
main.mainloop()