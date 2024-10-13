from tkinter import *

# create the main window
root = Tk()
# set the window size
root.geometry("500x600")
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

# board
board = {1: " ",2: " ",3: " ",
         4: " ",5: " ",6: " ",
         7: " ",8: " ",9: " "}

# global variable
turn = "X"
# for winning function to check who is winner x or o
def checkWinner(player):
    # columns1
    if (board[1] == board[4] and board[1] == board[7] and board[1] == player):
        return True
    if (board[2] == board[5] and board[2] == board[8] and board[2] == player):
        return True
    if (board[3] == board[6] and board[3] == board[9] and board[3] == player):
        return True
    # columns2
    if (board[1] == board[2] and board[1] == board[3] and board[1] == player):
        return True
    if (board[4] == board[5] and board[4] == board[6] and board[4] == player):
        return True
    if (board[7] == board[8] and board[7] == board[9] and board[7] == player):
        return True
    # columns3
    if (board[1] == board[5] and board[1] == board[9] and board[1] == player):
        return True
    if (board[3] == board[5] and board[3] == board[7] and board[3] == player):
        return True
    return False

# draw function 
def Draw():
    for position in board.keys():
        if board[position] == " ":
            return False
        
    return True   

# restart game
def restartGame():
    # remove the button texts

    for button in buttons:
        button["text"] = " "

    # remove the board 
    for position in board.keys():
        board[position] = " "
    # display the title after restart the game
    title_label = Label(frame1, text = "Tic-Tac-Toe", font = ("Arial", 30),bg="slategray4",fg="black")

    
    
# when click any button then X or O show into the button
def play(event):
    global turn
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if(button["text"] == " "): # if button empty then only can click 
        if (turn == "X"):
            button["text"] = "X"
            board[clicked] = button["text"]
            if checkWinner(turn):
                winningLabel = Label(frame2, text = f"{turn} wins the game",bg = "slategray4", font=("Arial",25))
                # this message showns on the middle
                winningLabel.grid(row = 1, column = 0, columnspan = 3)
            turn = "O"
        else:
            button["text"] = "O"
            board[clicked] = button["text"]
            if checkWinner(turn):
                winningLabel = Label(frame2, text = f"{turn} wins the game",bg = "slategray4", font=("Arial",25))
                winningLabel.grid(row = 1, column = 0, columnspan = 3)
            turn = "X"
        
        # check for draws
        if Draw():
            DrawLabel = Label(frame2, text = f"Draw the Game...",bg = "slategray4", font=("Arial",25))
            DrawLabel.grid(row = 1, column = 0, columnspan = 3)

    print(board)
    

# tic tac toe board
# first row
button0 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button0.grid(row = 0, column=0)
button0.bind("<Button-1>", play)

button1 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button1.grid(row = 0, column=1)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button2.grid(row = 0, column=2)
button2.bind("<Button-1>", play)

# second row
button3 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button3.grid(row = 1, column=0)
button3.bind("<Button-1>", play)

button4 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button4.grid(row = 1, column=1)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button5.grid(row = 1, column=2)
button5.bind("<Button-1>", play)

# third row
button6 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button6.grid(row = 2, column=0)
button6.bind("<Button-1>", play)

button7 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button7.grid(row = 2, column=1)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text= " ", width= 4, height=2,bg="gray16",font=("Arial",35), relief=RAISED, borderwidth=5)
button8.grid(row = 2, column=2)
button8.bind("<Button-1>", play)

# restart button
restartButton = Button(frame2, text = "Restart Game", width= 12, height= 1, font = ("Arial", 20), bg = "green", relief=RAISED, borderwidth=5, command= restartGame)
restartButton.grid(row = 4, column=0,columnspan=3)

# all buttons stored in a buttons list

buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8]

root.mainloop()