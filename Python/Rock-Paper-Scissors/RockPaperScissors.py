
import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("450x500")
window.configure(bg="#EAF4FF")
window.resizable(False, False)

# Scores
player_score = 0
computer_score = 0

# Game function
def play(player_choice):
    global player_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    player_label.config(text="You chose: " + player_choice)
    computer_label.config(text="Computer chose: " + computer_choice)

    if player_choice == computer_choice:
        result = "It's a Tie!"
        color = "orange"

    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        color = "green"
        player_score += 1

    else:
        result = "Computer Wins!"
        color = "red"
        computer_score += 1

    result_label.config(text=result, fg=color)
    score_label.config(
        text=f"Player: {player_score}   Computer: {computer_score}"
    )

# Reset function
def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_label.config(text="You chose: -")
    computer_label.config(text="Computer chose: -")
    result_label.config(text="Choose to Start!", fg="black")
    score_label.config(text="Player: 0   Computer: 0")

# Title
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF",
    fg="#174A7E"
)
title_label.pack(pady=25)

# Instructions
instruction_label = tk.Label(
    window,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 13),
    bg="#EAF4FF"
)
instruction_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(window, bg="#EAF4FF")
button_frame.pack(pady=20)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(
        button_frame,
        text=choice,
        font=("Arial", 12, "bold"),
        width=10,
        bg="#B8D9FF",
        command=lambda c=choice: play(c)
    ).pack(side="left", padx=5)

# Choices
player_label = tk.Label(
    window,
    text="You chose: -",
    font=("Arial", 13),
    bg="#EAF4FF"
)
player_label.pack(pady=8)

computer_label = tk.Label(
    window,
    text="Computer chose: -",
    font=("Arial", 13),
    bg="#EAF4FF"
)
computer_label.pack(pady=8)

# Result
result_label = tk.Label(
    window,
    text="Choose to Start!",
    font=("Arial", 18, "bold"),
    bg="#EAF4FF"
)
result_label.pack(pady=15)

# Score
score_label = tk.Label(
    window,
    text="Player: 0   Computer: 0",
    font=("Arial", 13, "bold"),
    bg="#EAF4FF"
)
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(
    window,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    bg="#FFB6B6",
    width=15,
    command=reset_game
)
reset_button.pack(pady=15)

# Run the GUI
window.mainloop()
