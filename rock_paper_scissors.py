import random
import tkinter as tk

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.ties_score = 0

        self.label_instruction = tk.Label(
            root,
            text="Choose Rock, Paper, or Scissors",
            font=("Helvetica", 14),
            name="game_instructions"
        )
        self.label_instruction.pack(pady=10)

        # Graphics mapping (using Emojis)
        self.graphics = {
            'rock': '✊',
            'rock': 'Rock (✊)',
            'paper': 'Paper (✋)',
            'scissors': 'Scissors (✌)'
        }

        # Frame for displaying graphical choices
        self.frame_display = tk.Frame(root)
        self.frame_display.pack(pady=10)

        self.lbl_player_graphic = tk.Label(self.frame_display, text="Unknown (❓)", font=("Segoe UI Emoji", 40))
        self.lbl_player_graphic.grid(row=0, column=0, padx=20)
        tk.Label(self.frame_display, text="You").grid(row=1, column=0)

        self.lbl_vs = tk.Label(self.frame_display, text="VS", font=("Helvetica", 20))
        self.lbl_vs.grid(row=0, column=1, padx=20)

        self.lbl_computer_graphic = tk.Label(self.frame_display, text="Unknown (❓)", font=("Segoe UI Emoji", 40))
        tk.Label(self.frame_display, text="Computer").grid(row=1, column=2)

        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.btn_rock = tk.Button(self.frame_buttons, text="Rock", width=10, command=lambda: self.play('rock'))
        self.btn_rock.grid(row=0, column=0, padx=5)

        self.btn_paper = tk.Button(self.frame_buttons, text="Paper", width=10, command=lambda: self.play('paper'))
        self.btn_paper.grid(row=0, column=1, padx=5)

        self.btn_scissors = tk.Button(self.frame_buttons, text="Scissors", width=10, command=lambda: self.play('scissors'))
        self.btn_scissors.grid(row=0, column=2, padx=5)

        self.label_result = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_result.pack(pady=20)

        self.label_score = tk.Label(root, text="Score - You: 0, Computer: 0, Ties: 0", font=("Helvetica", 12, "bold"))
        self.label_score.pack(pady=10)

        self.btn_quit = tk.Button(root, text="Quit", command=root.quit)
        self.btn_quit.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, player, computer):
        if player == computer:
            return 'tie'
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return 'player'
        else:
            return 'computer'

    def play(self, player_choice):
        """
        Executes a round of Rock-Paper-Scissors.

        Args:
            player_choice (str): The player's choice ('rock', 'paper', or 'scissors').

        This method:
        1. Gets the computer's random choice.
        2. Determines the winner.
        3. Updates the scores.
        4. Updates the result and score labels in the GUI.
        """
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)

        # Update graphics
        self.lbl_player_graphic.config(text=self.graphics[player_choice])
        self.lbl_computer_graphic.config(text=self.graphics[computer_choice])

        result_text = f"You chose: {player_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n"

        if winner == 'player':
            self.player_score += 1
            result_text += "You win this round!"
        elif winner == 'computer':
            self.computer_score += 1
            result_text += "Computer wins this round!"
        else:
            self.ties_score += 1
            result_text += "It's a tie!"

        self.label_result.config(text=result_text)
        self.label_score.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.ties_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
