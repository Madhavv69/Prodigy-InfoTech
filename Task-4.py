import tkinter as tk
from tkinter import messagebox


class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("600x600")

        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack(pady=20)

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            for j in range(9):
                bg_color = self.get_block_color(i, j)
                entry = tk.Entry(frame, width=5, font=('Arial', 18), justify='center', bd=2, relief='solid',
                                 highlightbackground="black", highlightcolor="black", highlightthickness=1, bg=bg_color)
                entry.grid(row=i, column=j, padx=1, pady=1, ipadx=5, ipady=5)
                self.entries[i][j] = entry

    def get_board(self):
        for i in range(9):
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit():
                    self.board[i][j] = int(val)
                else:
                    self.board[i][j] = 0

    def set_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.board[i][j]))

    def is_valid(self, num, pos):
        # Check row
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col

        return None

    def solve_sudoku(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve_sudoku():
                    return True

                self.board[row][col] = 0

        return False

    def solve(self):
        self.get_board()
        if self.solve_sudoku():
            self.set_board()
            messagebox.showinfo("Sudoku Solver", "Sudoku solved successfully!")
        else:
            messagebox.showwarning("Sudoku Solver", "No solution exists for the given Sudoku.")

    def get_block_color(self, row, col):
        colors = ['#FFFFCC', '#CCFFCC', '#CCFFFF', '#FFCCFF', '#FFCCCC', '#CCCCFF', '#FFCC99', '#99CCFF', '#CC99FF']
        return colors[(row // 3) * 3 + (col // 3)]


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
