import tkinter
from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, exitonclick
import os
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import time
import resultDisplay
import start_page
import confirm
from PIL import Image, ImageTk


def scanlogopage(vision):
    ws = Tk()
    ws.title("Betts Company")
    ws.geometry("1000x900")
    ws['background'] = '#DFDDD1'
    file_path = ""
    
    def open_file():
        file_w = askopenfilename(multiple=False,
                                 filetypes=[('Jpg Files', '*.jpg'), ('PNG Files', '*.png'), ('Jpeg Files', '*.jpeg')])
        # print(file_w)
        vision.set_input_image(file_w)
    
    def uploadFiles():
        pb1 = Progressbar(
            ws,
            orient=HORIZONTAL,
            length=300,
            mode='determinate'
        )
        pb1.place(relx=0.5, rely=0.4, anchor=CENTER)
        for i in range(5):
            ws.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        tkinter.Label(ws, text='File Uploaded Successfully!', font=('Sans', 24, BOLD), foreground='green',
                      bg='#DFDDD1').place(relx=0.5, rely=0.3, anchor=CENTER)
        col = 1  # start from column 1
        row = 3  # start from row 3
    
    for f in file_path:
        img = Image.open(f)  # read the image file
        img = img.resize((200, 200))  # new width & height
        img = ImageTk.PhotoImage(img)
        e1 = tkinter.Label(ws)
        e1.grid(row=row, column=col)
        e1.image = img
        e1['image'] = img  # garbage collection
        if (col == 3):  # start new line after third column
            row = row + 1  # start wtih next row
            col = 1  # start with first column
        else:  # within the same row
            col = col + 1  # increase to next column
    
    def nextPage():
        ws.destroy()
        confirm.confirmpage(vision, file_path)
        # resultDisplay.resultdisplay(vision)
    
    def prevPage():
        ws.destroy()
        start_page.startpage(vision)
    
    def kill():
        exit()
    
    adhar = tkinter.Label(
        ws,
        text='Upload logo in jpg format ',
        font=('Sans', 30, BOLD)
        , foreground='black',
        bg='#DFDDD1'
    )
    adhar.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    adharbtn = tkinter.Button(
        ws,
        text='Choose File', font=('Sans', 18, BOLD), padx=10, pady=10,
        command=lambda: open_file()
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
    
    exist = tkinter.Button(
        ws,
        text='Exit', font=('Sans', 20, BOLD), padx=20, pady=10,
        
        command=kill
    )
    exist.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    ws.mainloop()
