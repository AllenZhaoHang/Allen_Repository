'''
    TestRockPaperScissorsGame
    Hang Zhao
    11/26/2023
'''
import unittest
from tkinter import *
from tkinter import ttk
from random import *
from rock_paper_scissors_game import RockPaperScissorsGame


class TestRockPaperScissorsGame(unittest.TestCase):
    ''' TestRockPaperScissorsGame'''

    def setUp(self):
        self.root = Tk()
        self.game = RockPaperScissorsGame(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_init(self):
        ''' test_init'''
        assert 0 <= self.game.choose_number <= 2, f"Invalid value for choose_number: {self.game.choose_number}"
        self.assertIsInstance(self.game.label, Label)
        self.assertIsInstance(self.game.user_select, ttk.Combobox)
        self.assertIsInstance(self.game.button, Button)
        self.assertIsInstance(self.game.wl_label, Label)

    def test_spin(self):
        ''' test_spin'''
        self.game.user_select.set("Rock")
        self.game.spin()
        self.assertIn(self.game.choose_number, [0, 1, 2])
        self.assertIn(self.game.label["text"], ["rock", "paper", "scissors"])


if __name__ == '__main__':
    unittest.main()
