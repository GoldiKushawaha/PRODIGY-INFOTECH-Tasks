import tkinter as tk
from tkinter import messagebox
import random

# Random number to guess
number_to_guess = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < number_to_guess:
            result.set("Too low! Try again.")
        elif guess > number_to_guess:
            result.set("Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result.set("New game started. Guess the number!")

# GUI Setup
window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("350x250")
window.configure(bg="#f0f8ff")

tk.Label(window, text="Guess a number between 1 and 100", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(window, text="Check Guess", command=check_guess, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)

result = tk.StringVar()
result.set("Start guessing...")
tk.Label(window, textvariable=result, bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)

tk.Button(window, text="Reset Game", command=reset_game, bg="#f44336", fg="white", font=("Arial", 11)).pack(pady=10)

window.mainloop()