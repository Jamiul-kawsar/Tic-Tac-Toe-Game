from tkinter import *

# Create the main window
root = Tk()
root.geometry("500x600")
root.title("Tic Tac Toe")
root.configure(bg="slategray4")

frame1 = Frame(root)
frame1.pack()

title_label = Label(frame1, text="Tic-Tac-Toe", font=("Arial", 30), bg="slategray4", fg="black")
title_label.pack()

frame2 = Frame(root)
frame2.pack()

# Board setup
board = {i: " " for i in range(1, 10)}

# Global variables
turn = "X"
game_end = False
winningLabel = None
DrawLabel = None

# Original checkWinner function
def checkWinner(player):
    if (board[1] == board[4] and board[1] == board[7] and board[1] == player):
        return True
    if (board[2] == board[5] and board[2] == board[8] and board[2] == player):
        return True
    if (board[3] == board[6] and board[3] == board[9] and board[3] == player):
        return True
    if (board[1] == board[2] and board[1] == board[3] and board[1] == player):
        return True
    if (board[4] == board[5] and board[4] == board[6] and board[4] == player):
        return True
    if (board[7] == board[8] and board[7] == board[9] and board[7] == player):
        return True
    if (board[1] == board[5] and board[1] == board[9] and board[1] == player):
        return True
    if (board[3] == board[5] and board[3] == board[7] and board[3] == player):
        return True
    return False

# Original Draw function
def Draw():
    for position in board.keys():
        if board[position] == " ":
            return False
    return True   

def restartGame():
    global game_end, winningLabel, DrawLabel, turn
    game_end = False
    turn = "X"
    
    # Reset the board buttons
    for button in buttons:
        button["text"] = " "
        
    # Reset the board dictionary
    for position in board.keys():
        board[position] = " "
    
    # Remove the winning and draw labels if they exist
    if winningLabel:
        winningLabel.grid_forget()
        winningLabel = None
    if DrawLabel:
        DrawLabel.grid_forget()
        DrawLabel = None

    # Reset title label in case it was changed
    title_label.config(text="Tic-Tac-Toe")

# Minimax algorithm
def minimax(board, isMaximizing):
    if checkWinner("O"):
        return 1
    if checkWinner("X"):
        return -1
    if Draw():
        return 0

    bestScore = -100 if isMaximizing else 100
    for key in board.keys():
        if board[key] == " ":
            board[key] = "O" if isMaximizing else "X"
            score = minimax(board, not isMaximizing)
            board[key] = " "
            bestScore = max(score, bestScore) if isMaximizing else min(score, bestScore)
    return bestScore

def playComputer():
    global turn
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key
    board[bestMove] = "O"
    buttons[bestMove - 1]["text"] = "O"
    if checkWinner("O"):
        global winningLabel
        winningLabel = Label(frame2, text="O wins the game", bg="slategray4", font=("Arial", 25))
        winningLabel.grid(row=1, column=0, columnspan=3)
        game_end = True

def play(event):
    global turn, game_end, winningLabel, DrawLabel
    if game_end:
        return
    button = event.widget
    clicked = buttons.index(button) + 1

    if button["text"] == " ":
        button["text"] = turn
        board[clicked] = turn
        if checkWinner(turn):
            winningLabel = Label(frame2, text=f"{turn} wins the game", bg="slategray4", font=("Arial", 25))
            winningLabel.grid(row=1, column=0, columnspan=3)
            game_end = True
            return
        elif Draw():
            DrawLabel = Label(frame2, text="Draw the Game...", bg="slategray4", font=("Arial", 25))
            DrawLabel.grid(row=1, column=0, columnspan=3)
            game_end = True
            return
        turn = "O" if turn == "X" else "X"
        if turn == "O":
            playComputer()
            turn = "X"

# Tic-tac-toe board buttons
buttons = []
for i in range(9):
    button = Button(frame2, text=" ", width=4, height=2, bg="gray16", font=("Arial", 35), relief=RAISED, borderwidth=5)
    button.grid(row=i//3, column=i % 3)
    button.bind("<Button-1>", play)
    buttons.append(button)

# Restart button
restartButton = Button(frame2, text="Restart Game", width=12, height=1, font=("Arial", 20), bg="green", relief=RAISED, borderwidth=5, command=restartGame)
restartButton.grid(row=4, column=0, columnspan=3)

root.mainloop()
