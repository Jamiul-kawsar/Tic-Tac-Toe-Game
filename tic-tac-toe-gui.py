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
game_end = False
winningLabel = None
DrawLabel = None
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
        # all turn after anyone won the game
        #if not(checkWinner(player)):
            #return False
    return True   

# restart game
def restartGame():
    global game_end, winningLabel, DrawLabel
    game_end = False
    # remove the button texts
    for button in buttons:
        button["text"] = " "

    # remove the board 
    for position in board.keys():
        board[position] = " "
    # display the title after restart the game
    title_label = Label(frame1, text = "Tic-Tac-Toe", font = ("Arial", 30),bg="slategray4",fg="black")
    if winningLabel:
        winningLabel.grid_forget()
    if DrawLabel:
        DrawLabel.grid_forget()

#minimax algorithm
def minimax(board, isMaximizing):
    if checkWinner("O"):
        return 1
    if checkWinner("X"):
        return -1
    if Draw():
        return 0
    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score = minimax(board, False) # false because of now it's player turn 
                board[key] == " "
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score = minimax(board, True) # True because of now it's computer turn 
                board[key] == " "
                if score < bestScore:
                    bestScore = score
        
        return bestScore

# computer play automaticly
def playComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score = minimax(board, False) # false because of now it's player turn 
            board[key] == " "
            if score > bestScore:
                bestScore = score
                bestMove = key

    board[bestMove] = "O"

    
# the main function 
# when click any button then X or O show into the button
if __name__ == "__main__":
    def play(event):
        global turn, game_end, winningLabel, DrawLabel
        if game_end == True:
            return
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
                    game_end = True
                turn = "O"
                playComputer()
                turn = "X"
            else:
                button["text"] = "O"
                board[clicked] = button["text"]
                if checkWinner(turn):
                    winningLabel = Label(frame2, text = f"{turn} wins the game",bg = "slategray4", font=("Arial",25))
                    winningLabel.grid(row = 1, column = 0, columnspan = 3)
                    game_end = True
                turn = "X"
            
            # check for draws
            if Draw():
                DrawLabel = Label(frame2, text = f"Draw the Game...",bg = "slategray4", font=("Arial",25))
                DrawLabel.grid(row = 1, column = 0, columnspan = 3)
                game_end = True

        print(board)


# tic tac toe board buttons
buttons = []
for i in range(9):
    button = Button(frame2, text=" ", width=4, height=2, bg="gray16", font=("Arial", 35), relief=RAISED, borderwidth=5)
    button.grid(row=i//3, column=i % 3)
    button.bind("<Button-1>", play)
    buttons.append(button)

# restart button
restartButton = Button(frame2, text = "Restart Game", width= 12, height= 1, font = ("Arial", 20), bg = "green", relief=RAISED, borderwidth=5, command= restartGame)
restartButton.grid(row = 4, column=0,columnspan=3)

root.mainloop()