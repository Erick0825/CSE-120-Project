import tkinter
from tkinter import *
from turtle import exitonclick
import os
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time



ws = Tk()
ws.title("Betts Company")
ws.geometry("1920x1080")
ws['background'] = '#DFDDD1'

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

def nextPage():
    ws.destroy()
    import resultDisplay

def prevPage():
    ws.destroy()
    import start_page


adhar = Label(
    ws, 
    text='Upload logo in jpg format '
    )
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)


upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)

PrevPage = Button(
    ws, 
    text="Previous Page", 
    command=prevPage
    )
PrevPage.grid(row=5, column=0, pady=10)

NextPage = Button(
    ws, 
    text="Next Page", 
    command=nextPage
    )
NextPage.grid(row=5, column=1, pady=10)

exist=Button(
    ws,
    text='Exit',
    command=exitonclick
    )
exist.grid(row=5, columnspan=3, pady=10)


ws.mainloop()
