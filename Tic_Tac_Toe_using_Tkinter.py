import tkinter as tk
from tkinter import messagebox
from functools import partial  # Import partial to avoid lambda issues

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables to store player turns and board state
player = "X"
board = [["", "", ""], ["", "", ""], ["", "", ""]]

# Function to check for a winner or a tie
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    # Check for a tie (if all cells are filled)
    for row in board:
        if "" in row:
            return None
    return "Tie"

# Function to reset the board
def reset_game():
    global player, board
    player = "X"
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    for button in buttons:
        button.config(text="", state="normal")

# Function to handle button click
def on_button_click(row, col, btn):
    global player
    if btn["text"] == "":
        btn.config(text=player)
        board[row][col] = player
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

# Create buttons for the grid
buttons = []
for row in range(3):
    for col in range(3):
        btn = tk.Button(root, text="", font=("Arial", 40), width=5, height=2)
        btn.config(command=partial(on_button_click, row, col, btn))  # Use partial to pass arguments
        btn.grid(row=row, column=col)
        buttons.append(btn)

# Start the main Tkinter loop
root.mainloop()