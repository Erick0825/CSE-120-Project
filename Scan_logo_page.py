import tkinter
from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, exitonclick
import os
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time



ws = Tk()
ws.title("Betts Company")
ws.geometry("1000x900")
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

def kill():
    exit()

adhar = tkinter.Label(
    ws, 
    text='Upload logo in jpg format ',
    font=('Sans', 30,BOLD)
    ,foreground='black',
    bg= '#DFDDD1'
)
adhar.place(relx=0.5, rely=0.2, anchor=CENTER)

adharbtn = tkinter.Button(
    ws, 
    text ='Choose File', font=('Sans', 18, BOLD), padx=10, pady=10,
    command = lambda:open_file()
    ) 
adharbtn.place(relx=0.6, rely=0.5, anchor=CENTER)


upld = tkinter.Button(
    ws, 
    text='Upload Files', font=('Sans', 18, BOLD), padx=10, pady=10,
    command=uploadFiles
    )
upld.place(relx=0.6, rely=0.6, anchor=CENTER)

PrevPage = tkinter.Button(
    ws, 
    text="Previous Page", font=('Sans', 18, BOLD), padx=10, pady=10,
    command=prevPage
    )
PrevPage.place(relx=0.4, rely=0.6, anchor=CENTER)

NextPage = tkinter.Button(
    ws, 
    text="Next Page", font=('Sans', 18, BOLD), padx=10, pady=10,
  
    command=nextPage
    )
NextPage.place(relx=0.4, rely=0.5, anchor=CENTER)

exist=tkinter.Button(
    ws,
    text='Exit', font=('Sans', 20, BOLD), padx=20, pady=10,
    
    command=kill
    )
exist.place(relx=0.5, rely=0.9, anchor=CENTER)


ws.mainloop()
