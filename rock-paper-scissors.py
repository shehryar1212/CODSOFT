import tkinter as tk
from tkinter import messagebox
import random

my_font={"System 20 bold"}
def play_game(player_choice):
    computer_choice = random.choice(list(choices.keys()))
    result = ''
    
    if player_choice == computer_choice:
        result = 'Tie'
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        result = 'You Win!'
        update_scores(1)
    else:
        result = 'Computer Wins!'
        update_scores(2)
    
    player_label.config(text=f'You chose: {choices[player_choice]}',font="System 20 bold")
    computer_label.config(text=f'Computer chose: {choices[computer_choice]}',font="System 20 bold")
    result_label.config(text=result)

def update_scores(winner):
    global player_score, computer_score
    if winner == 1:
        player_score += 1
    elif winner == 2:
        computer_score += 1
    
    player_score_label.config(text=f'Your Score: {player_score}',font="System 20 bold")
    computer_score_label.config(text=f'Computer Score: {computer_score}',font="System 20 bold")
    
    if player_score == 10 or computer_score == 10:
        end_game()

def end_game():
    winner = "You" if player_score > computer_score else "Computer"
    messagebox.showinfo("Game Over", f"{winner} Win!")
    root.destroy()

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

player_score = 0
computer_score = 0

player_score_label = tk.Label(root, text=f'Your Score: {player_score}',font="System 20 bold")
player_score_label.pack()

computer_score_label = tk.Label(root, text=f'Computer Score: {computer_score}',font="System 20 bold")
computer_score_label.pack()

player_label = tk.Label(root, text="You chose: ",font="System 20 bold")
player_label.pack()

computer_label = tk.Label(root, text="Computer chose: ",font="System 20 bold")
computer_label.pack()

result_label = tk.Label(root, text="",font="System 20 bold",fg="red")
result_label.pack()
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game(1),font="System 20 bold")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game(2),font="System 20 bold")
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game(3),font="System 20 bold")
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()
