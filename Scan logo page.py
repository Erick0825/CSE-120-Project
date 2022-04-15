import tkinter
from tkinter import *
from turtle import exitonclick



main = Tk()
main.geometry("400x200")
main['background'] = '#8a0602'


main.title("Betts Company")

#User is able to upload a logo
button = tkinter.Button(main, text="Upload Logo", highlightbackground='#3E4149')
button.grid(row=1, column=0)
button.pack(side='bottom')
button.place(x=0, y=0)


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
    

