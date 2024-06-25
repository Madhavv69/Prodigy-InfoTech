import tkinter as tk
from tkinter import messagebox
import random


class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="I have selected a random number between 1 and 100.\nTry to guess the number!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.feedback_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                self.feedback_label.config(text="")
                messagebox.showinfo("Congratulations!",
                                    f"You've guessed the number {self.number_to_guess} correctly in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
