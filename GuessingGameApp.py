import tkinter as tk
import random

class GuessingGameApp:
    def __init__(self, root):  # Fixed constructor name
        self.root = root
        self.root.title("🎯 Guessing Game")
        self.root.geometry("350x250")

        # Random number
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Title label
        self.title_label = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

        # Entry for guess
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Submit button
        self.submit_btn = tk.Button(root, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.submit_btn.pack(pady=5)

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        # Attempts label
        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        # Restart button
        self.restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), command=self.restart_game)
        self.restart_btn.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.number_to_guess:
                self.feedback_label.config(text="📉 Too low! Try again.", fg="blue")
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="📈 Too high! Try again.", fg="orange")
            else:
                self.feedback_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} attempts.", fg="green")
        except ValueError:
            self.feedback_label.config(text="❌ Please enter a valid number.", fg="red")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")

# Run app
if __name__ == "__main__":  # Fixed main check
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()