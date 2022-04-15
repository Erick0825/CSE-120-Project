import tkinter
from tkinter import *
from turtle import exitonclick
import os


main = Tk()
main.geometry("400x200")
main['background'] = '#8a0602'
filename = form['filename']


main.title("Betts Company")

#User is able to upload a logo
button = tkinter.Button(main, text="Upload Logo", highlightbackground='#3E4149')
button.grid(row=1, column=0)
button.pack(side='bottom')
button.place(x=0, y=0)

#User is able to select and choose what scan logo they want to upload
if  filename.filename:
     fn = os.path.basename(fileitem.filename)
        open(fn, 'wb').write(fileitem.file.read())
        print("File '%s' was uploaded" % fn)
    else :
        print("No file was uploaded")

#returns user to the main menu
exit = tkinter.Button("Would you like to return to the main page? Yes or no\n", highlightbackground='#3E4149')
exit = exit.mainloop()
exit.grid(row=1, column=0)
exit.pack(side='bottom')
exit.place(x=0, y=0)


if exit == "yes" or "y":
    player = False
else:
    main() 
    mainloop()
 
