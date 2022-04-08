import tkinter
from tkinter import *
from turtle import exitonclick

main = Tk()
main.geometry("400x200")
main['background'] = '#8a0602'

main.title("Result")

if bool(True):
    label = tkinter.Label(text="Pass", background="#00FF00")
else:
    label = tkinter.Label(text="Fail", background="#FF0000")