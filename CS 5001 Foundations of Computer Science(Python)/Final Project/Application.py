'''
    Application class, main entrance
    Hang Zhao
    11/26/2023
'''
from rock_paper_scissors_game import RockPaperScissorsGame
from tkinter import *


def main():
    ''' main function '''
    root = Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
