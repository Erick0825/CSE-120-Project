import tkinter
from tkinter import *
from turtle import exitonclick



main = Tk()
main.geometry("400x200")
main['background'] = '#8a0602'



main.title("Betts Company")

button = tkinter.Button(main, text="Scan Logo", highlightbackground='#3E4149')
button.grid(row=1, column=0)
button.pack(side='bottom')

exit = tkinter.Button("Would you like to return to the main page? Yes or no\n", highlightbackground='#3E4149')
exit = exit.lower()

if exit == "yes" or "y":
    player = False
else:
    main() 
 