import tkinter as tk
import random
from tkinter import simpledialog, messagebox

# Constants
DOOR_CELL = "door"
SWEETS_ROOM_CELL = "sweets"
HIDDEN_ROOM_CELL = "hidden"
ILLUMINATED_CELL = "illuminated"
GHOST_ROOM_CELL = "ghost"

ENIGMAS = [
    "How many years are in a century?",
    "What word is a synonym for happiness?",
    "What is the largest animal in the world?",
    "How many continents are there in the world?",
    "In what year was your country's independence?"
]

ENIGMAS_ANSWERS = {
    "How many years are in a century?": "100",
    "What word is a synonym for happiness?": "joy",
    "What is the largest animal in the world?": "blue whale",
    "How many continents are there in the world?": "7",
    "In what year was your country's independence?": "variable"
}

GHOST_QUESTIONS_ANSWERS = {
    "What is the color of a ghost?": "white",
    "In what place is a ghost supposed to inhabit?": "cemetery",
    "What holiday is most related to ghosts?": "Halloween",
    "What typical figure scares ghosts according to legends?": "scarecrow"
}

class HalloweenGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Halloween Game")
        self.player = self.get_valid_player_name()
        self.path = []
        self.remaining_attempts = 4
        self.instructions = "Instructions:\n\n1. Navigate through the 4x4 mansion to find the sweets room.\n\n2. " \
                             "Each time you move to a hidden cell, you must answer a riddle or ghost question.\n\n3. " \
                             "You have 4 attempts to move in the direction you choose (north, south, east, or west).\n\n4. " \
                             "If you answer a riddle or ghost question correctly, the cell will light up.\n\n5. " \
                             "If you find the sweets room, you win, {}! Have fun!".format(self.player)
        self.create_mansion()
        self.create_interface()
        self.show_instructions()

    def get_valid_player_name(self):
        while True:
            player_name = simpledialog.askstring("Welcome", "Enter your name:")
            if player_name is None:
                self.window.quit()
            elif player_name.strip() != "":
                return player_name
            else:
                messagebox.showerror("Invalid Name", "Please enter a valid name.")

    def create_mansion(self):
        # Create the mansion as a 4x4 matrix with hidden cells
        self.mansion = [[HIDDEN_ROOM_CELL] * 4 for _ in range(4)]

    def create_interface(self):
        # Create the graphical interface with buttons for each room
        for row in range(4):
            for column in range(4):
                button = tk.Button(self.window, text=" ", font=("Arial", 16),
                                   command=lambda r=row, c=column: self.make_move(r, c))
                button.grid(row=row, column=column, sticky="nsew")  # Use sticky to make buttons expand with window

        # Hacer las filas y columnas expansibles
        for i in range(4):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def ask_yes_no_question(self, title, question):
        while True:
            response = simpledialog.askstring(title, question)
            if response is None:
                # Si se cierra la ventana, salir del juego
                self.window.quit()
            elif response.lower() in ["yes", "no"]:
                return response.lower()
            else:
                messagebox.showerror("Invalid Response", "Please enter 'Yes' or 'No'.")

    def show_instructions(self):
        response_instructions = self.ask_yes_no_question("Instructions", "Do you want to see the instructions?")
        if response_instructions is None:
            self.window.quit()
        elif response_instructions.lower() == "yes":
            messagebox.showinfo("Instructions", self.instructions)
        else:
            messagebox.showinfo("Let's Begin!", "Let the game begin!")

    def make_move(self, row, column):
        if not self.path:  # If path is empty, it's the first click
            self.path.append((row, column))
            self.generate_door_and_sweets()
        elif self.remaining_attempts == 0:
            return
        else:
            current_row, current_column = self.path[-1]
            if row != current_row and column != current_column:
                # User can only move vertically or horizontally
                return
            self.remaining_attempts -= 1
            self.path.append((row, column))
            self.update_interface()
            if self.mansion[row][column] == SWEETS_ROOM_CELL:
                messagebox.showinfo("Congratulations!", "You found the sweets room, {}! You win!".format(self.player))
                self.retry_game()
            elif self.mansion[row][column] == HIDDEN_ROOM_CELL:
                if random.random() < 0.1:
                    # Ghost appears
                    self.handle_ghost_encounter(row, column)
                else:
                    # Normal question from the hidden room
                    self.handle_enigma_encounter(row, column)

    def handle_ghost_encounter(self, row, column):
        # Ghost appears
        ghost_question_1 = random.choice(list(GHOST_QUESTIONS_ANSWERS.keys()))
        correct_ghost_answer_1 = GHOST_QUESTIONS_ANSWERS[ghost_question_1]
        user_answer_1 = simpledialog.askstring("Ghost", ghost_question_1)
        if user_answer_1 is None:
            self.window.quit()
        elif user_answer_1.lower() == correct_ghost_answer_1.lower():
            # First question answered correctly, ask the second question
            ghost_question_2 = random.choice(list(GHOST_QUESTIONS_ANSWERS.keys()))
            correct_ghost_answer_2 = GHOST_QUESTIONS_ANSWERS[ghost_question_2]
            user_answer_2 = simpledialog.askstring("Ghost", ghost_question_2)
            self.handle_answer(ghost_question_2, user_answer_2, correct_ghost_answer_2, row, column)
        else:
            self.handle_answer(ghost_question_1, user_answer_1, correct_ghost_answer_1, row, column)

    def handle_enigma_encounter(self, row, column):
        enigma_question = random.choice(ENIGMAS)
        correct_enigma_answer = ENIGMAS_ANSWERS[enigma_question]
        user_answer = simpledialog.askstring("Riddle", enigma_question)
        self.handle_answer(enigma_question, user_answer, correct_enigma_answer, row, column)

    def handle_answer(self, question, user_answer, correct_answer, row, column):
        if user_answer is None:
            # Count cancellation as an incorrect answer
            messagebox.showerror("Incorrect Answer!", "Cancelled answer. Game Over!")
            self.retry_game()
        elif user_answer.lower() == correct_answer.lower():
            self.mansion[row][column] = ILLUMINATED_CELL
            self.update_interface()
            messagebox.showinfo("Correct Answer!", "You answered correctly. You can continue.")
        else:
            messagebox.showerror("Incorrect Answer!", "Incorrect answer. Game Over!")
            self.retry_game()

    def retry_game(self):
        self.remaining_attempts = 4
        self.path = []
        self.create_mansion()
        self.update_interface()

    def update_interface(self):
        for row, rooms_row in enumerate(self.mansion):
            for column, room_type in enumerate(rooms_row):
                if room_type == DOOR_CELL:
                    text = "🚪"
                elif room_type == SWEETS_ROOM_CELL:
                    text = "🍭"
                elif room_type == ILLUMINATED_CELL:
                    text = "✨"
                elif room_type == GHOST_ROOM_CELL:
                    text = "👻"
                else:
                    text = " "
                self.window.grid_slaves(row=row, column=column)[0].config(text=text)

    def generate_door_and_sweets(self):
        door_row, door_column = self.path[0]
        sweets_row, sweets_column = self.generate_random_position_with_distance(door_row, door_column, 3)
        self.mansion[door_row][door_column] = DOOR_CELL
        self.mansion[sweets_row][sweets_column] = SWEETS_ROOM_CELL
        self.update_interface()

    def generate_random_position_with_distance(self, base_row, base_column, distance):
        # Generate a random position with a minimum distance from the base position
        while True:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if abs(row - base_row) + abs(column - base_column) >= distance and \
                    self.mansion[row][column] == HIDDEN_ROOM_CELL:
                return row, column

# Create the main window
main_window = tk.Tk()
halloween_game = HalloweenGame(main_window)
main_window.mainloop()