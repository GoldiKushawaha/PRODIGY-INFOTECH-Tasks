import tkinter as tk
from tkinter import messagebox

# --- Backtracking Sudoku Solver ---
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# --- GUI Functions ---
def solve():
    grid = []
    try:
        for i in range(9):
            row = []
            for j in range(9):
                val = entries[i][j].get()
                if val == "":
                    row.append(0)
                else:
                    row.append(int(val))
            grid.append(row)

        if solve_sudoku(grid):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(grid[i][j]))
        else:
            messagebox.showinfo("Result", "No solution exists for this Sudoku.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter only digits 1-9 or leave empty.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# --- Main GUI Window ---
root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#e8f0fe")
root.geometry("400x500")

tk.Label(root, text="Sudoku Solver", font=("Arial", 18, "bold"), bg="#e8f0fe").pack(pady=10)

frame = tk.Frame(root)
frame.pack()

entries = []

for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(frame, width=3, font=('Arial', 14), justify='center', bd=2, relief="ridge")
        e.grid(row=i, column=j, padx=2, pady=2)
        row.append(e)
    entries.append(row)

tk.Button(root, text="Solve", command=solve, bg="#4caf50", fg="white", font=("Arial", 12), width=10).pack(pady=10)
tk.Button(root, text="Clear", command=clear_grid, bg="#f44336", fg="white", font=("Arial", 12), width=10).pack()

root.mainloop()