import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import confirm
my_w = Tk()
my_w.title("Betts Company")
my_w.geometry("1000x900")
my_w['background'] = '#DFDDD1'
my_font1=('Sans', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Files & display',width=30,font=my_font1,bg='#DFDDD1')  
l1.place(relx=0.5, rely=0.05, anchor=CENTER)
b1 = tk.Button(my_w, text='Upload Files',font=('Sans', 18, 'bold'), padx=10, pady=10, 
command = lambda:upload_file())
b1.place(relx=0.4, rely=0.95, anchor=CENTER)

def nextPage():
        my_w.destroy()
        confirm.confirmpage(vision, f_types)


NextPage = tk.Button(
    my_w, 
    text="Next Page", font=('Sans', 18, 'bold'), padx=10, pady=10,
    
    command=lambda: nextPage()
    )
NextPage.place(relx=0.6, rely=0.95, anchor=CENTER)

def upload_file():
    
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'), ('Jpeg Files','*.jpeg')]
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((200,200)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column       
def nextPage():
    my_w.destroy()
    confirm.confirmpage(vision, f_types)          
my_w.mainloop()  # Keep the window open