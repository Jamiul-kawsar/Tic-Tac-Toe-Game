from tkinter import *

# create the main window
root = Tk()
# set the window size
root.geometry("500x500")
# set the window title
root.title("Tic Tac Toe")
# set the window color
root.configure(bg = "slategray4")

frame1 = Frame(root)
frame1.pack()

title_label = Label(frame1, text = "Tic-Tac-Toe", font = ("Arial", 30),bg="slategray4",fg="black")
title_label.pack()


frame2 = Frame(root)
frame2.pack()
# global variable
turn = 1

# when click any button then X or O show into the button
def play(event):
    global turn
    button = event.widget
    
    if (turn == 1):
        button["text"] = "X"
        turn = not(turn)
    else:
        button["text"] = "O"
        turn = not(turn)


# tic tac toe board
# first row
button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 0, column=0)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 0, column=1)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 0, column=2)
button0.bind("<Button-1>", play)

# second row
button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 1, column=0)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 1, column=1)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 1, column=2)
button0.bind("<Button-1>", play)

# third row
button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 2, column=0)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 2, column=1)
button0.bind("<Button-1>", play)

button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 2, column=2)
button0.bind("<Button-1>", play)

root.mainloop()