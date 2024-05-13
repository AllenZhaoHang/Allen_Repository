'''
    This is a Python code that creates a Rock-Paper-Scissors
    game using the tkinter library. The program generates a
    random number to represent the computer's choice of rock,
    paper or scissors, and then compares it to the user's choice,
    which is selected through a dropdown menu. The program then
    displays the result of the game and updates the label accordingly.
    Hang Zhao
    11/26/2023
'''
from tkinter import *
from tkinter import ttk
from random import *


class RockPaperScissorsGame:
    ''' class RockPaperScissorsGame '''

    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Rock-Paper-Scissors-Game")

        self.list = ["rock", "paper", "scissors"]
        self.choose_number = randint(0, 2)
        print(self.choose_number)  # For testing if it works

        self.label = Label(self.root, text="Computer ", width=20,
                           height=4, font=("algerian", 15))
        self.label.pack()

        self.user_select = ttk.Combobox(
            self.root, value=["Rock", "Paper", "Scissors"])
        self.user_select.pack()

        self.button = Button(self.root, text="Spin", command=self.spin)
        self.button.pack()

        self.wl_label = Label(self.root, text="", width=40,
                              height=4, font=("algerian", 12))
        self.wl_label.pack()

    def spin(self):
        ''' spin function '''
        self.choose_number = randint(0, 2)
        self.label.config(text=self.list[self.choose_number])

        user_select_value = 0
        if self.user_select.get() == "Rock":
            user_select_value = 0
            print(user_select_value)
        elif self.user_select.get() == "Paper":
            user_select_value = 1
            print(user_select_value)
        elif self.user_select.get() == "Scissors":
            user_select_value = 2
            print(user_select_value)

        if user_select_value == 0:
            if self.choose_number == 0:
                self.wl_label.config(text="Tie! - "+" Computer:Bad luck")
            elif self.choose_number == 1:
                self.wl_label.config(
                    text="YOU Loose - "+" Computer: I am better ")
            elif self.choose_number == 2:
                self.wl_label.config(
                    text="YOU Won - "+" Computer: You won by luck")

        elif user_select_value == 1:
            if self.choose_number == 1:
                self.wl_label.config(text="Tie! - "+" Computer: Nice game")
            elif self.choose_number == 0:
                self.wl_label.config(text="YOU Won - " +
                                     " Computer: Shit how you are better")
            elif self.choose_number == 2:
                self.wl_label.config(text="YOU Loose - "+" Computer: booo")

        elif user_select_value == 2:
            if self.choose_number == 2:
                self.wl_label.config(text="Tie!")
            elif self.choose_number == 0:
                self.wl_label.config(text="YOU Loose - " +
                                     " Computer: I am playing this game since i was born")
            elif self.choose_number == 1:
                self.wl_label.config(text="YOU Won")
